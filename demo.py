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

easingMultiple(motionrest,3)
time.sleep(1)
easingMultiple(motionalert,1.8)
time.sleep(1)
easingMultiple(motionforward,1)
time.sleep(.5)
printer.println("hello")
time.sleep(.2)
easingMultiple(motionoffer,1)
time.sleep(.5)
printer.feed(4)
time.sleep(1.5)
easingMultiple(motionalert,1.8)
time.sleep(4)
easingMultiple(motionrest,3)
time.sleep(.5)
