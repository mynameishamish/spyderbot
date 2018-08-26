
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

def temp():
    while True:
        # print("temp")
        m1temp = robot.m1.present_temperature
        m2temp = robot.m2.present_temperature
        m3temp = robot.m3.present_temperature
        if m1temp is not None and m2temp is not None:
            print('m1Temp={0:0.1f}*C m2Temp={1:0.1f}*C m3Temp={2:0.1f}*C'.format(m1temp, m2temp, m3temp))
            # Send humidity and temperature feeds to Adafruit IO
            m1temp = '%.2f'%(m1temp)
            m2temp = '%.2f'%(m2temp)
            m3temp = '%.2f'%(m3temp)

            aio.send(m1temp_feed.key, str(m1temp))
            aio.send(m2temp_feed.key, str(m2temp))
            aio.send(m3temp_feed.key, str(m3temp))
        # else:
        #     print('Failed to get DHT22 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')
        # Timeout to avoid flooding Adafruit IO
        time.sleep(timeout)



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
