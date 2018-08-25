
import time
import math
import numpy

from easing import *
from motions import *
from Adafruit_Thermal import *


printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)



for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.set_moving_speed = 200


easingMultiple(motionrest, 3)
time.sleep(1)

easingMultiple(motionalert, 3)
time.sleep(2)

easingMultiple(motionforward, 3)
time.sleep(2)

easingMultiple(motionoffer, 3)
time.sleep(2)

easingMultiple(motionrest, 3)
