
import time
import math
import numpy

from easing import *
from motions import *


#
# print("starting")
#
# resting(40, 40, 40)
#
# up(40, 40, 40)
#
# alert(40, 40, 40)
#
# resting(40, 40, 40)
#
# print("finished")




# EasePos Stuff Below

print("starting Easepos")

motionrest= [
    [robot.m1, easeInOutQuart, robot.m1.present_position, 0] ,
    [robot.m2 ,easeInOutQuart, robot.m2.present_position, 20.3] ,
    [robot.m3 ,easeInOutQuart, robot.m3.present_position, -6]]

motionalert= [
    [robot.m1, easeInOutQuart, robot.m1.present_position, 0] ,
    [robot.m2 ,easeInOutQuart, robot.m2.present_position, 30] ,
    [robot.m3 ,easeInOutQuart, robot.m3.present_position, 23.3]]

motionforward= [
    [robot.m1, easeInOutQuart, robot.m1.present_position, 0] ,
    [robot.m2 ,easeInOutQuart, robot.m2.present_position, 45] ,
    [robot.m3 ,easeInOutQuart, robot.m3.present_position, 59]]

motionnew1= [
    [robot.m4 , x, robot.m4.present_position, 30] ,
    [robot.m5 , x, robot.m5.present_position, 40.3]]

motionnew2= [
    [robot.m4 , x, robot.m4.present_position, 90] ,
    [robot.m5 , x, robot.m5.present_position, 90]]

<<<<<<< HEAD
# print("rest")
# easingMultiple(motionrest, 1)
# time.sleep(1)
#
# print("alert")
# easingMultiple(motionalert, 1)
# time.sleep(2)
#
# print("motionforward")
# easingMultiple(motionforward, 1)
# time.sleep(2)
#
# print("rest")
# easingMultiple(motionrest, 1)
# time.sleep(1)

robot.m4.goal_position = 20.3
robot.m5.goal_position = -6

time.sleep(2)

print("new1")
easingMultiple(motionnew1, 2)
=======
print("rest")
easingMultiple(motionrest, 2)
time.sleep(1)

print("alert")
easingMultiple(motionalert, 2)
time.sleep(2)

print("motionforward")
easingMultiple(motionforward, 2)
time.sleep(.1)

print("rest")
easingMultiple(motionrest, 2)
>>>>>>> parent of 1d3d311... sucessfully merged into motions.py
time.sleep(1)

print("new2")
easingMultiple(motionnew2, 2)
time.sleep(4)

print("done")

robot.m4.moving_speed = 500
robot.m5.moving_speed = 500

robot.m4.goal_position = 90
robot.m5.goal_position = 90

time.sleep(3)

robot.m4.goal_position = -90
robot.m5.goal_position = -90

time.sleep(3)
