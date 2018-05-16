from Adafruit_Thermal import *
import sys
printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)
def printChunk(s):
    printer.setSize('L')
    printer.println(s)
    printer.feed(2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        printChunk(sys.argv[1])
    else:
        printChunk("TEST")
