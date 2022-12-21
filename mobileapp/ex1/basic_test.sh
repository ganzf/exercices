#!/bin/bash

function status {
    response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
    echo $response
}

function json {
    response=$(curl -sb -H "Accept: application/json" "$1")
    echo $response
}

st=$(status "http://localhost:8000/")
success=0
error=""

function check_error {
    echo $success
    if [ "$success" == "1" ]; then
        echo "Error: $error"
        exit $success
    fi
}

##
## Check server status is 200 OK on /
##
echo $st
if [ "$st" == "200" ]; then
    echo "Server available !"
else
    success=1
    error="Server not responding on /: $st"
fi

check_error

##
## Check server devices list is empty on /devices
##
json localhost:8000/devices?filter=any > output.txt
diff output.txt expected_1.txt > /dev/null
if [ $? -eq 0 ]; then
    echo "Devices list OK"
else
    success=1
    error="Invalid response for devices?filter=any"
fi

check_error

if [ $success -eq 1 ]; then
    echo "Test failed"
    echo $error
else
    echo "Test passed"
    echo "Bravo :)"
fi
