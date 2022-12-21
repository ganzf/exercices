# Imports go here

class DeviceStreamProvider:
    def __init__(self, server, device):
        self.server = server
        self.device = device
        self.last_frame = None
        self.rotation = None

    def set_rotation(self):
        if self.server.state == States.CAPTURING:
            try:
                orientation = device.get_interface_orientation()
                if orientation is not None:
                    rotation = 0
                    if orientation == 2:
                        rotation = 180
                    elif orientation == 3:
                        rotation = 90
                    elif orientation == 4:
                        rotation = 270
                    if rotation != self.rotation:
                        self.rotation = rotation
                        log.info("Got new rotation with value {}".format(self.rotation))
                        url = 'http://127.0.0.1:5678/orientation'
                        data = json.dumps({"device_id": self.device.id, "orientation": self.rotation})
                        req = http.Request(url, data, {'Content-Type': 'application/json'})
                        f = http.urlopen(req)
                        f.close()
            except Exception as e:
                log.error("An error occured while retrieving orientation: {}".format(e))

    def get_stream_frame(self):
        if self.server.state == States.CAPTURING:
            try:
                png_tmp = cStringIO.StringIO()
                png_tmp.write(self.device.take_screenshot())
                img = Image.open(png_tmp)
                if img.mode == "RGBA":
                    img = img.convert("RGB")
                if self.rotation is not None:
                    img = img.rotate(self.rotation, expand=True)
                jpg_tmp = cStringIO.StringIO()
                img.save(jpg_tmp, 'JPEG')
                jpg_tmp.seek(0, 0)
                data = jpg_tmp.read()
                data_size = len(data)
                jpg_tmp.close()
                png_tmp.close()
                return (data, data_size)
            except Exception as e:
                self.log.error("Got error in get_stream_frame from DeviceStreamProvider : {}".format(e.message))
                return None
        return None

    def single_frame(self):
        if self.server.state == States.CAPTURING:
            if self.device is None:
                log.error("Device client is None")
                return None
            self.set_rotation()
            frame = self.get_stream_frame()
            if frame != None:
                self.last_frame = frame
            return self.get_last_frame()
        return None

    def get_last_frame(self):
        if not self.last_frame:
            log.error("Got no last frame")
        return self.last_frame