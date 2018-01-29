
import time
import math
import numpy

from easing import *
from motions import *



print("starting")

resting(40, 40, 40)

up(40, 40, 40)

alert(40, 40, 40)

resting(40, 40, 40)

print("finished")




# EasePos Stuff Below

print("starting Easepos")

motionalert1= [
    [robot.m1, easeInOutQuart, robot.m1.present_position, 0] ,
    [robot.m2 ,easeInOutQuart, robot.m2.present_position, 20.3] ,
    [robot.m3 ,easeInOutQuart, robot.m3.present_position, 20]]

motionalert2= [
    [robot.m1, easeInOutQuart, robot.m1.present_position, 0] ,
    [robot.m2 ,easeInOutQuart, robot.m2.present_position, 20.3] ,
    [robot.m3 ,easeInOutQuart, robot.m3.present_position, 6]]

motionforward= [
    [robot.m1, easeInOutQuart, robot.m1.present_position, 0] ,
    [robot.m2 ,easeInOutQuart, robot.m2.present_position, 45] ,
    [robot.m3 ,easeInOutQuart, robot.m3.present_position, 58]]



robot.m1.goal_position = 0
robot.m2.goal_position = 20.3
robot.m3.goal_position = -6
print("Rest")
time.sleep(3)

print("alert1")
easingMultiple(motionalert1, 3)
time.sleep(1)

print("alert2")
easingMultiple(motionalert2, 2)
time.sleep(1)

print("motionforward")
easingMultiple(motionforward, 2)
time.sleep(.1)

robot.m1.goal_position = 0
robot.m2.goal_position = 20.3
robot.m3.goal_position = -6
print("Rest")
time.sleep(3)
