import time
import math
import numpy
import os

from easing import *
from motions import *
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

for m in robot.motors:
    m.compliant = False
    m.set_moving_speed = 10
robot.m1.moving_speed = 200
robot.m2.moving_speed = 40
robot.m3.moving_speed = 40

print("starting")

alert()

run = True

while run:
    print('Choose a motion:')
    command = raw_input()
    if command == "offer":
        offer()

    elif command == "rest":
        resting()

    elif command == "alert":
        alert()

    elif command == "forward":
        forward()

    elif command == "exit":
        run=False

    overheating()

resting()
