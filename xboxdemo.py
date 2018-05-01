import time
import math
import numpy
import os

from easing import *
from motions import *
from Adafruit_Thermal import *
import xbox

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

speed=300

for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.set_moving_speed = 10
robot.m1.moving_speed = 200
robot.m2.moving_speed = 40
robot.m3.moving_speed = 40

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
		return remap(inp, 0,1,100,149)

def remapBase(inp):
	return remap(inp, -1, 1, -48, 40)
def display(topic):
	os.system("pkill chromium")
	string="DISPLAY=:0 chromium-browser --kiosk --disable-infobars tv.giphy.com/"+topic+" &"
	os.system(string)
display("cat")
time.sleep(4)
display("dog")


joy = xbox.Joystick()
flag= False
control=False

print "Xbox controller demo: Press Back button to exit"
print("Press start to take control")

while not flag:
    while control:
	    robot.m2.goal_position= remapNeck(joy.rightY())
	    robot.m3.goal_position = remapHead(joy.leftY())
	    overheating()

	    if joy.rightTrigger() and robot.m1.present_position>-48:
	    	robot.m1.moving_speed=speed**2 *joy.rightTrigger()
	    	robot.m1.goal_position= robot.m1.present_position-4
	    
	    if joy.leftTrigger() and robot.m1.present_position<40:
	    	robot.m1.moving_speed=speed**2 *joy.leftTrigger()
	    	robot.m1.goal_position= robot.m1.present_position+4
	    time.sleep(.0001)
	    
	    if joy.A():
	    	display("cat")
	    	print("HEYOOOOOO")

	    	# printer.println("HEYOOOOOO")
	    	# printer.feed(3)
	    	robot.m2.moving_speed = 200
	    	robot.m3.moving_speed=200
	    	easingMultiple(motionoffer, 2)
	    	time.sleep(2)
	    	robot.m3.moving_speed=40
	    	robot.m2.moving_speed = 40
	    

	    if joy.B(): 
	    	display("dog")
	    	print("HEYOOOOOO")
	    	printer.println("doggo what!")
	    	printer.feed(3)
	    	robot.m2.moving_speed = 200
	    	robot.m3.moving_speed=200
	    	easingMultiple(turnaway, 1.5)
	    	time.sleep(1.5)
	    	robot.m3.moving_speed=40
	    	robot.m2.moving_speed = 40
	    	printer.println("HEYOOOOOO")
	    	printer.feed(3)
	    
	    if joy.X(): 
	    	display("nah")
	    	print("nope!")
	    	printer.println("Nope")
	    	printer.feed(3)
	    	robot.m2.moving_speed = 200
	    	robot.m3.moving_speed=200
	    	# easingMultiple(musicup, 1.5)
	    	easing(robot.m1, easeInOutSine, -20, .2)
	    	easing(robot.m1, easeInOutSine, 20, .4)
	    	easing(robot.m1, easeInOutSine, -20, .4)
	    	easing(robot.m1, easeInOutSine, 20, .4)
	    	easing(robot.m1, easeInOutSine, -4, .4)
	    	time.sleep(1.85)
	    	robot.m3.moving_speed=40
	    	robot.m2.moving_speed = 40
	    if joy.Y(): 
	    	display("penguin")
	    	print("HEYOOOOOO")
	    	printer.println("Pingu or Penguin?")
	    	robot.m2.moving_speed = 200
	    	robot.m3.moving_speed=200
	    	easing(robot.m3, easeInOutSine, 110, .2)
	    	easing(robot.m3, easeInOutSine, 90, .4)
	    	easing(robot.m3, easeInOutSine, 110, .4)
	    	easing(robot.m3, easeInOutSine, 90, .4)
	    	easing(robot.m3, easeInOutSine, 110, .4)
	    	
	    	time.sleep(5)
	    	robot.m3.moving_speed=40
	    	robot.m2.moving_speed = 40
	    
	    if joy.rightBumper():
        	inp=raw_input("giphy giph:")
        	display(inp)
        	printer.println("oh look! a "+ inp)
        	printer.feed(3)





	    if joy.Start():
	    	control=False
	    	time.sleep(.4)
	    	print("control= False")


	# if max([m.present_temperature for m in robot.motors])>=72:
	# 	overheating()
    overheating()
    if joy.Back():
        flag=True
    if joy.Start():
        control=True
        time.sleep(.4)
    	print("control= True")			
resting()
# Close out when done
joy.close()
