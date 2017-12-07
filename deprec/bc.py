from ax12 import Ax12

import time
import sys

self = Ax12();

veryslow = 50
slow = 100
medium = 150
fast = 200

# Sleeping Movement
def sleep():
    self.moveSpeed(3,225,slow)
    self.moveSpeed(4,880,slow)
    time.sleep(1)

# Listening Movement
def listen():
    self.moveSpeed(3,350,slow)
    self.moveSpeed(4,600,slow)
    time.sleep(1)

# Slow movement
def longNod():
    self.moveSpeed(4,600,slow)
    time.sleep(0.3)
    self.moveSpeed(4,650,slow)
    time.sleep(0.3)
    self.moveSpeed(4,600,slow)
    time.sleep(0.3)

# # Fast movement
def shortNod():
    self.moveSpeed(4,640, slow)
    time.sleep(0.25)
    self.moveSpeed(4,600, slow)
    time.sleep(0.25)

# Simple backchanneling
def simpleBC():
    longNod()
    time.sleep(0.5)
    shortNod()

# Emphatice backchanneling
def complexBCforward():
    self.moveSpeed(4,600,slow)
    self.moveSpeed(3,350,slow)
    time.sleep(0.3)
    self.moveSpeed(4,615,veryslow)
    self.moveSpeed(3,365,veryslow)
    time.sleep(0.4)
    self.moveSpeed(4,600,veryslow)
    self.moveSpeed(3,350,veryslow)
    time.sleep(0.3)

# Emphatice backchanneling
def complexBCbackward():
    self.moveSpeed(3,350,slow)
    time.sleep(0.3)
    self.moveSpeed(4,630,slow)
    self.moveSpeed(3,370,slow)
    time.sleep(0.3)
    self.moveSpeed(4,600,veryslow)
    self.moveSpeed(3,350,veryslow)
    time.sleep(0.3)

def shock():
	self.moveSpeed(4,600,slow)
	self.moveSpeed(3,350,slow)
	time.sleep(0.3)
	self.moveSpeed(4,740,medium)
	self.moveSpeed(3,250,slow)
	time.sleep(1.5)
	self.moveSpeed(4,840,medium)
	time.sleep(1.5)
	self.moveSpeed(4,760,veryslow)
	time.sleep(2.5)
	self.moveSpeed(3,350,veryslow)
	self.moveSpeed(4,600,slow)


def sad():
    self.moveSpeed(4,800,veryslow/2)
    time.sleep(5.0)
    self.moveSpeed(3,225,veryslow)
    self.moveSpeed(4,900,veryslow)
    time.sleep(1.5)
    self.moveSpeed(4,820,veryslow)
    time.sleep(0.25)
    self.moveSpeed(4,600,slow)
    time.sleep(0.5)
    self.moveSpeed(3,350,slow)
    time.sleep(1)


listen()
time.sleep(1)
sad()

#time.sleep(3)
#complexBCforward()
