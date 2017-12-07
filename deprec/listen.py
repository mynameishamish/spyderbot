from ax12 import Ax12

import time
import sys

self = Ax12();

speed1 = 100
speed2 = 200


# min/max 3 = 200/550
# min/max 4 = 550/1000
# sleep 3 = 550, 4 = 1000

while True:

    self.moveSpeed(2,700,speed2)    
    self.moveSpeed(3,350,speed1)
    self.moveSpeed(4,650,speed2)

    time.sleep(2)

    sys.exit();












# self.readTemperature(1)

# time.sleep(2)
