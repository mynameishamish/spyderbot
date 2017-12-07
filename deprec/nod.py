from ax12 import Ax12

import time
import sys

self = Ax12();

veryslow = 50
slow = 100
medium = 150
fast = 200

# Slow movement
def longNod():
    self.moveSpeed(4,650,slow)
    time.sleep(0.3)
    self.moveSpeed(4,700,slow)
    time.sleep(0.3)
    self.moveSpeed(4,650,slow)
    time.sleep(0.3)

# # Fast movement
def shortNod():
    self.moveSpeed(4,700, slow)
    time.sleep(0.25)
    self.moveSpeed(4,650, slow)
    time.sleep(0.25)

# Simple backchanneling
def simpleBC():
    longNod()
    time.sleep(0.5)
    shortNod()

simpleBC()

#time.sleep(3)
#complexBCforward()
