#!/usr/bin/python

from Adafruit_Thermal import *
from PIL import Image
import time

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)
current = time.time()
printer.printImage(Image.open('upload/upload.png'), False)
print(time.time() - current)

printer.feed(1)