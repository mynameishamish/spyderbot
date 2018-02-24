
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

x = easeInOutSine

# EasePos Stuff Below

print("starting Easepos")

motionrest= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -77] ,
    [robot.m3 , x, robot.m3.present_position, -73]]

motionalert= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -65] ,
    [robot.m3 , x, robot.m3.present_position, 135]]

motionforward= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -45] ,
    [robot.m3 , x, robot.m3.present_position, 149]]

motionoffer= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -26] ,
    [robot.m3 , x, robot.m3.present_position, 112]]


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

resting(30,30,30)

time.sleep(2)

print("alert")
easingMultiple(motionalert, 1.5)
time.sleep(1)

print("forward")
easingMultiple(motionforward, 1)
time.sleep(1)

print("rest")
easingMultiple(motionrest, 1.5)
time.sleep(1)

print("offer")
easingMultiple(motionoffer, 2)
time.sleep(1)

print("rest")
easingMultiple(motionrest, 1.5)
time.sleep(1)


print("done")
