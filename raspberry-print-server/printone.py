from Adafruit_Thermal import *
from PIL import Image

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=99999999)
printer.printImage(Image.open("upload/9.png"), False)
