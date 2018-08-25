import time
import math
import numpy

from easing import *
from motions import *
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

print(robot.m1.present_position)
print(robot.m2.present_position)
print(robot.m3.present_position)


resting()
time.sleep(1)
alert()
time.sleep(1)
forward()
time.sleep(.5)
printer.println("hello")
time.sleep(.2)
offer()
time.sleep(.5)
printer.feed(2)
time.sleep(1.5)
alert()
time.sleep(4)
resting()
time.sleep(.5)
