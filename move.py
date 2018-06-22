import time
import math
import numpy
import os
import sys

from easing import *
from motions import *
from Adafruit_Thermal import *

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
    overheating()

    command = raw_input()
    command = sys.stdin.readline()
    command = command.split('\n')[0]
    if command == "hello":
        sys.stdout.write("You said hello!\n")
    elif command == "goodbye":
        sys.stdout.write("You said goodbye!\n")
        run = False
    else:
        sys.stdout.write("Sorry, I didn't understand that.\n")
    sys.stdout.flush()

resting()
