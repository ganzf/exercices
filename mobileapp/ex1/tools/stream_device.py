import sys
import time
import random

crash = False

device_id = sys.argv[1]
device_name = sys.argv[2]

while not crash:
    # generate rgb triple named color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    print(device_id + ":\t" + device_name + "\t\t[" + "OK" + "]\t" + str(color))
    time.sleep(0.5)
    # one every thousand times
    if random.randint(0, 1000) < 10:
        crash = True

## for 5 seconds
t = time.time()
while time.time() - t < 5:
    print(device_id + ":\t" + device_name + "\t\t[" + "KO" + "]\t" + "()")
    time.sleep(0.5)