from ax12 import Ax12

import time
import sys

self = Ax12();

speed1 = 100
speed2 = 200



while True:


    self.moveSpeed(2,500,speed1)
    self.moveSpeed(3,225,speed1)
    self.moveSpeed(4,880,speed2)

    time.sleep(2)

    sys.exit();








# self.readTemperature(1)

# time.sleep(2)
