
import time
import math
import numpy
import threading
import os

from easing import *
from motions import *
from Adafruit_Thermal import *
from Adafruit_IO import Client, Feed


printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

timeout = 6

ADAFRUIT_IO_KEY = os.environ.get('adafruit_io_key')
ADAFRUIT_IO_USERNAME = 'mynameishamish'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

m1temp_feed = aio.feeds('spyderbot.base')
m2temp_feed = aio.feeds('spyderbot.neck')
m3temp_feed = aio.feeds('spyderbot.head')


for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.set_moving_speed = 5


t = threading.Timer(.5, temp)
t.start()

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
