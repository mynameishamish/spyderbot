
import time
import math
import numpy

from easing import *
from motions import *
from Adafruit_Thermal import *


# printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)



for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.set_moving_speed = 200

# resting()
# limp()
# livly()
# resting()
# concur()


# print("returning home")
# easingMultiple(motionrest, 1)
# time.sleep(2)
# print("compliant")

# for m in robot.motors: # Note that we always provide an alias for all motors.
#     m.compliant = True
#     m.set_moving_speed = 200
# time.sleep(20)
#
# print("starting")
# resting(50, 50, 50)

# # print("alert")
# # easingMultiple(motionalert, 1)


print("forward")
easingMultiple(motionforward, 3)
time.sleep(1)

print("returning home")
easingMultiple(motionrest, 3)
time.sleep(2)

print("forward")
easingMultiple(motionforward, 3)
time.sleep(2)

print("returning home")
easingMultiple(motionrest, 3)
time.sleep(2)

print("done")
