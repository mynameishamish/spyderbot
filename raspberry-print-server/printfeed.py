from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=99999999)
printer.begin()
printer.feed(-5)
