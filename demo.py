
import time
import math
import numpy

from easing import *
from motions import *
from Adafruit_Thermal import *


printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)



for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.set_moving_speed = 5


easingMultiple(motionrest, 2)
time.sleep(1)

easingMultiple(motionalert, .8)
time.sleep(2)

easingMultiple(motionforward, .8)
easingMultiple(leftpos, .8)
easingMultiple(rightpos, 1)
time.sleep(1)
shake()
time.sleep(.4)
nod()
time.sleep(.5)

printer.println("hello")
easingMultiple(motionoffer, .5)
printer.feed(3)
time.sleep(1.5)

easingMultiple(motionalert, 1)
time.sleep(1)

easingMultiple(motionrest, 1.2)
