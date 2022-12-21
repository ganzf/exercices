# Ex1 - Device Manager

You have to create an API with the language you want (python3 or go for example).

## Step 1: Api Basic Specs

Routes:
GET / => "Hello World"
GET /health => JSON{ status: "OK" | "ERROR", error?: string }
GET /version => JSON{ version: "1.0.0" }
GET /devices => []Device as JSON
GET /devices/:name => Device as JSON

When displaying information about a device, your API should display:
- A name (string)
- An osName (iOS | Android)
- A version (string)
- A status (OK | KO)
- A streaming status (OK | KO)
- An error (optionnal string)

To know the available devices, your server will have to use the provided script: detect_devices.py and read its output.
To load the devices status in your server memory, it should not be necessary to request /devices.
You should check the status of devices everytime you receive a request on /devices/:name but not when requesting on /devices.

## Step 2: Updating devices

Modify the detect_devices script to return status OK instead of status KO for both devices.
Add an asynchronous routine that updates the devices status every 10 secondes.



