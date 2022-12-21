class Device:
    def __init__(self, name: str) -> None:
        self.name = "Device_Name"
        self.osName = name
        self.status = "KO"
        self.version = "13.2"

    def Print(self):
        print({"name": self.name, "status": self.status, "osName": self.osName, "version": self.version})

devices = []

devices.append(Device("iOS"))
devices[0].name = "IOS_Device"
devices.append(Device("Android"))
devices[1].version = "14.2"
devices[1].name = "Android_Device"

for device in devices:
    device.Print()