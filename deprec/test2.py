from ax12 import Ax12

import time

self = Ax12();

while True:

    self.move(1,200)

    time.sleep(2)

    self.move(1,400)

    time.sleep(2)



# self.readTemperature(1)

# time.sleep(2)
