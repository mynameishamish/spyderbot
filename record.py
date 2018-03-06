import time
import numpy
import math
from easing import *
from motions import *

import pypot.robot


amp = 30
freq = 0.5

robot = pypot.robot.from_config(spyder_config)

# Put the robot in its initial position
for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    # m.goal_position = 0

# Wait for the robot to actually reach the base position.
time.sleep(2)
# pos = 0


# #recording
import time
import pypot.robot


from pypot.primitive.move import MoveRecorder, Move, MovePlayer


feed in robot, framerate, motors
move_recorder = MoveRecorder(robot, 70, robot.motors)
#make motors compliant
robot.compliant = True
#record for 10 seconds
print("RECORD")
move_recorder.start()
time.sleep(7)
move_recorder.stop()
print("STOPPING")

time.sleep(2)
# playback
with open('trial1.move', 'w') as f:
    move_recorder.move.save(f)
print("PLAYING")

with open('trial1.move') as f:
    m = Move.load(f)


robot.compliant = False

move_player = MovePlayer(robot, m)
#starting playback, sleep for duration of playback otherwise you will get a thread issue
move_player.start()
time.sleep(7)
print("PLAYED")
