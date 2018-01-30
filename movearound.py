
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
    [robot.m1 , x, robot.m1.present_position, 0] ,
    [robot.m2 , x, robot.m2.present_position, 20.3] ,
    [robot.m3 , x, robot.m3.present_position, -6]]

motionalert= [
    [robot.m1 , x, robot.m1.present_position, 0] ,
    [robot.m2 , x, robot.m2.present_position, 30] ,
    [robot.m3 , x, robot.m3.present_position, 40.3]]

motionforward= [
    [robot.m1 , x, robot.m1.present_position, 0] ,
    [robot.m2 , x, robot.m2.present_position, 45] ,
    [robot.m3 , x, robot.m3.present_position, 59]]



print("rest")
easingMultiple(motionrest, 1)
time.sleep(1)

print("alert")
easingMultiple(motionalert, 1)
time.sleep(2)

print("motionforward")
easingMultiple(motionforward, 1)
time.sleep(2)

print("rest")
easingMultiple(motionrest, 1)
time.sleep(1)
