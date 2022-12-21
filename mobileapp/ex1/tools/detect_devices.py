class Device:
    def __init__(self, name: str) -> None:
        self.name = name
        self.status = "OFF"

    def Print(self):
        print({"name": self.name, "status": self.status})

devices = []

devices.append(Device("iOS"))
devices.append(Device("Android"))

for device in devices:
    device.Print()