
import time
import math
import numpy

from easing import *
from motions import *

robot.m2.goal_position = 30

time.sleep(1)

robot.m2.goal_position = 40

time.sleep(1)

resting(2, 2, 2)

up(2, 2, 2)

alert(2, 2, 2)

resting(2, 2, 2)

time.sleep(1)

easing(robot.m1, easeInQuad, 40, 2)
