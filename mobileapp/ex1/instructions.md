# Ex1 - Device Manager

You have to create an API with the language you want (python3 or go for example).

## Step 1: Api Basic Specs

Routes:
GET / => "Hello World"
GET /health => JSON{ status: "OK" | "ERROR", error?: string }
GET /version => JSON{ version: "1.0.0" }
GET /devices => []Device as JSON

When displaying information about a device, your API should display:
- A name (string)
- An osName (iOS | Android)
- A version (string)
- A status (OK | KO)
- A streaming status (OK | KO)
- An error (optionnal string)

To know the available devices, your server will have to use the provided script: detect_devices.py and read its output.

## Step 2:

