#!/bin/bash

./fizzbuzz 16 > output.txt
diff output.txt expected.txt
success=$?
if [ $success -eq 0 ]; then
    echo "Bravo !"
else
    echo "Oh non... ca ne marche pas"
fi

