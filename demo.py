import time
import math
import numpy

from easing import *
from motions import *
from Adafruit_Thermal import *

resting()
time.sleep(1)
alert()
time.sleep(1)
forward()
time.sleep(.5)
printer.println('hello')
time.sleep(.2)
offer()
time.sleep(2)
alert()
time.sleep(4)
resting()
time.sleep(.5)
