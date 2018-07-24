import time
import math
import numpy

from easing import *
from motions import *
from Adafruit_Thermal import *

for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.set_moving_speed = 200

print("resting")
easingMultiple(motionrest, .8)
time.sleep(.5)
