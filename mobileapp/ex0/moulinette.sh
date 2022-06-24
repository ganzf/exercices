#!/bin/bash

if [ -z "./fizzbuzz" ]; then
    ./fizzbuzz 16 > output.txt
    diff output.txt expected.txt
    success=$?
    if [ $success -eq 0 ]; then
        echo "Bravo !"
    else
        echo "Oops, something went wrong..."
    fi
else
    echo "fizzbuzz not found !"
    exit 1
fi
