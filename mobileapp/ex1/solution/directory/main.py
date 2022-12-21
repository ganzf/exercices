import uuid
import threading
import time
import subprocess
from fastapi import FastAPI, Request

app = FastAPI()

class Device:
    def __init__(self, name, uuid, device_type):
        self.name = name
        self.uuid = uuid
        self.type = device_type
        self.status = "on"

    def getType(self):
        return self.type

    def setStatus(self, status):
        self.status = status

class Data:
    devices: list[Device] = []

data = Data()

@app.get("/")
async def root(request: Request):
    return {}

@app.get("/devices")
async def devices(request: Request, filter: str = None):
    list = []
    print (filter)
    for device in data.devices:
        if device.getType() == filter or filter == None or filter == "any":
            list.append(device)
    return {"devices": list}

def detect_device():
    print("Detecting devices...")
    output = subprocess.check_output("./detect_devices")
    lines = str(output).splitlines()
    found = []
    # Each line is type uuid name
    for line in lines:
        type = line.split(" ")[0]
        uuid = line.split(" ")[1]
        name = line.split(" ")[2]
        found.append(uuid)
        exists = list(filter(lambda d: (d.uuid == uuid), data.devices))
        if not exists:
            data.devices.append(Device(name, uuid, type))
    for device in data.devices:
        if device.uuid not in found:
            device.setStatus("off")

def detect_device_thread():
    while True:
        detect_device()
        time.sleep(1)

# data.devices.append(Device("device1", uuid.uuid4(), "light"))
# On server startup, launch detect_device_thread
threading.Thread(target=detect_device_thread).start()