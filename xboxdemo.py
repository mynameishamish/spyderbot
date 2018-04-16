import time
import math
import numpy

from easing import *
from motions import *
from Adafruit_Thermal import *
import xbox


# printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.set_moving_speed = 10
robot.m1.moving_speed = 200
robot.m2.moving_speed = 40
robot.m3.moving_speed = 40

print("starting")

def remapNeck(OldValue):

	OldMin, OldMax, NewMin, NewMax, = -1, 1, -67, -36,
	OldRange = (OldMax - OldMin)  
	NewRange = (NewMax - NewMin)  
	NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
	return NewValue

def remapHead(OldValue):
	OldMin, OldMax, NewMin, NewMax, = -1, 1, 83, 139, 
	OldRange = (OldMax - OldMin)  
	NewRange = (NewMax - NewMin)  
	NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
	return NewValue

def remapBase(OldValue):
	OldMin, OldMax, NewMin, NewMax, = -1, 1, -48, 40, 
	OldRange = (OldMax - OldMin)  
	NewRange = (NewMax - NewMin)  
	NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
	return NewValue

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)
    
joy = xbox.Joystick()
print(joy.Back())
flag= False
control=False

print "Xbox controller demo: Press Back button to exit"
while not flag:
    while control:

	    robot.m2.goal_position= remapNeck(joy.rightY())
	    robot.m3.goal_position = remapHead(joy.leftY())

	    if joy.rightTrigger() and robot.m1.present_position>-48:
	    	robot.m1.goal_position= robot.m1.present_position-4
	    if joy.leftTrigger() and robot.m1.present_position<40:
	    	robot.m1.goal_position= robot.m1.present_position+4
	    time.sleep(.0001)
	    
	    if joy.Start():
	    	control=False
	    	time.sleep(.4)
	    	print("control= False")

    if joy.Back():
        flag=True
    if joy.Start():
        control=True
        time.sleep(.4)
    	print("control= True")			

# Close out when done
joy.close()
