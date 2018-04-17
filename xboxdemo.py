import time
import math
import numpy

from easing import *
from motions import *
from Adafruit_Thermal import *
import xbox

err=ErrorHandlr()
# printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

speed=300

for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.set_moving_speed = 10
robot.m1.moving_speed = 200
robot.m2.moving_speed = 75
robot.m3.moving_speed = 155

print("starting")

def remap(OldValue,OldMin, OldMax, NewMin, NewMax):
	OldRange = (OldMax - OldMin)  
	NewRange = (NewMax - NewMin)  
	NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
	return NewValue

def remapNeck(inp):
	if inp<=0:
		return remap(inp, -1,0,-77,-65)
	else:
		return remap(inp, 0,1,-65,-36)


def remapHead(inp):
	if inp<=0:
		return remap(inp,-1,0,83,100)
	else:
		return remap(inp, 0,1,100,139)

def remapBase(inp):
	return remap(inp, -1, 1, -48, 40)

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

def overheating():
    print("motors are overheating")
    print("going to limp rest")
    resting()
    limp()

    while True:
        inp=raw_input("for current temps press t and hit enter \nto re-engage motors type m:")
        if inp=="t":
            print([(m.name, m.present_temperature) for m in robot.motors])
        if inp=="m":
            print("re-engageing motors")
            livly()
        else:
            print("invalid input")

joy = xbox.Joystick()
flag= False
control=False

print "Xbox controller demo: Press Back button to exit"
print("Press start to take control")

while not flag:
    while control:

	    robot.m2.goal_position= remapNeck(joy.rightY())
	    robot.m3.goal_position = remapHead(joy.leftY())
	    if max([m.present_temperature for m in robot.motors])>=72:
	    	overheating()

	    if joy.rightTrigger() and robot.m1.present_position>-48:
	    	robot.m1.moving_speed=speed**2 *joy.rightTrigger()
	    	robot.m1.goal_position= robot.m1.present_position-4
	    
	    if joy.leftTrigger() and robot.m1.present_position<40:
	    	robot.m1.moving_speed=speed**2 *joy.leftTrigger()
	    	robot.m1.goal_position= robot.m1.present_position+4
	    time.sleep(.0001)
	    
	    if joy.A(): 
	    	robot.m2.moving_speed = 200
	    	robot.m3.moving_speed=200
	    	easingMultiple(motionoffer, 2)
	    	robot.m3.moving_speed=40
	    	robot.m2.moving_speed = 40
	    if joy.Start():
	    	control=False
	    	time.sleep(.4)
	    	print("control= False")


	# if max([m.present_temperature for m in robot.motors])>=72:
	# 	overheating()
    if joy.Back():
        flag=True
    if joy.Start():
        control=True
        time.sleep(.4)
    	print("control= True")			

# Close out when done
joy.close()
