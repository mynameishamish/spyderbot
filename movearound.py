
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


#
print("starting")
resting(50, 50, 50)

<<<<<<< HEAD
print("alert")
easingMultiple(motionalert, 1)


=======
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
print("rest")
easingMultiple(motionrest, 1.5)
time.sleep(1)

>>>>>>> 81c34ec6921d54c383bf5cd32c8bed6a1b16a84e
print("forward")
easingMultiple(motionforward, 1.5)
time.sleep(1)

<<<<<<< HEAD
print("returning home")
easingMultiple(motionrest, 1)
time.sleep(2)

# print("forward")
# easingMultiple(motionforward, .5)
# time.sleep(2)

# print("returning home")
# easingMultiple(motionrest, .5)
# time.sleep(2)

=======
print("offer")
easingMultiple(motionoffer, 1.5)
time.sleep(2)

printer.println("heckin'")
printer.feed(5)

time.sleep(2)

print("moving home")
easingMultiple(motionrest, 1.5)
time.sleep(2)

# print("rest")
# easingMultiple(motionrest, 1.5)
# time.sleep(1)


>>>>>>> 81c34ec6921d54c383bf5cd32c8bed6a1b16a84e
print("done")
