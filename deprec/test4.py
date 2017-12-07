from ax12 import Ax12

import time

self = Ax12();

speed1 = 100
speed2 = 50



while True:



    self.moveSpeed(3,200,speed1)

    time.sleep(2)


    self.moveSpeed(3,500,speed1)

    time.sleep(5)



    self.moveSpeed(4,520,speed1)

    time.sleep(5)

    self.moveSpeed(4,1000,speed1)

    time.sleep(2)










# self.readTemperature(1)

# time.sleep(2)
