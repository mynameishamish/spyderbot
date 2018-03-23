
import time
import math
import numpy

from easing import *
from motions import *
from Adafruit_Thermal import *


# printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

x = easeInOutSine




#
# print("starting")
#
# resting(40, 40, 40)
#
# up(40, 40, 40)
#
# alert(40, 40, 40)
#
# resting(40, 40, 40)
#
# print("finished")



# print("rest")
# easingMultiple(motionrest, 1)
# time.sleep(1)
#
# print("alert")
# easingMultiple(motionalert, 1)
# time.sleep(2)
#
# print("motionforward")
# easingMultiple(motionforward, 1)
# time.sleep(2)
#
# print("rest")
# easingMultiple(motionrest, 1)
# time.sleep(1)

print("forward")
easingMultiple(motionforward, .25)
time.sleep(1)

print("offer")
easingMultiple(motionoffer, .5)
time.sleep(2)

# printer.println("heckin'")
# printer.feed(5)

time.sleep(2)
print("moving home")
easingMultiple(motionrest, .5)
time.sleep(2)

# print("rest")
# easingMultiple(motionrest, 1.5)
# time.sleep(1)


print("done")
