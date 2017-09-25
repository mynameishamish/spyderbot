spyder_config = {
    'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['base'],
            'port': 'auto'
        }
    },
    'motorgroups': {
        'base': ['m1', 'm2', 'm3']
    },
    'motors': {
        'm1': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 2,
            'angle_limit': [-90.0, 90.0],
            'offset': 0.0
        },
        'm2': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 3,
            'angle_limit': [4.0, 50.0],
            'offset': 0.0
        },
        'm3': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 4,
            'angle_limit': [0.0, 38.0],
            'offset': 0.0
        }
    }
}
import time
import numpy

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


# print(robot.m1.present_position)
# robot.m1.goal_position = pos
# time.sleep(.02)
# print(robot.m1.present_position)


# # Do the sinusoidal motions for 10 seconds
# t0 = time.time()

# while True:
#     t = time.time() - t0

#     if t > 10:
#         break

#     pos = amp * numpy.sin(2 * numpy.pi * freq * t)

#     robot.m1.goal_position = pos


#     time.sleep(0.02)
def easeInQuad(t):
    return t**2

def easeInOutBack(t, s=1.70158):
    t *= 2
    if t < 1:
        s *= 1.525
        return 0.5 * (t * t * ((s + 1) * t - s))
    else:
        t -= 2
        s *= 1.525
        return 0.5 * (t * t * ((s + 1) * t + s) + 2)
#
motion1 ={
    'm1': [robot.m1, easeInQuad, 90, 2]
    }

def easeInOutQuad(t, b, c, d):
	t /= float(d/2)
	if t < 1:
		return c/2*t*t + b
	t-=1
	return -c/2 * (t*(t-2) - 1) + b

def easeInOutSine(t, b, c, d):
	return -c/2 * (math.cos(math.pi*t/d) - 1) + b

def easing(motor, e_fn, final_position, duration):

    t0=time.time()
    d= duration
    b= motor.present_position
    c=final_position-b

    while True:
        t=float(time.time()-t0)
        if t>=d:
            break
        pos =e_fn(t, b, c, d)
        motor.goal_position=pos
        print(motor.present_position)


        time.sleep(0.02)

easing(robot.m1, easeInOutQuad, 44, .5)
easing(robot.m2, easeInOutQuad, 44, 1.01)
easing(robot.m3, easeInOutQuad, 38, 1.01)

time.sleep(2)

easing(robot.m2, easeInOutQuad, 7, 1)
easing(robot.m3, easeInOutQuad, 0.1, 1)


#easing(robot.m1, easeInOutBack, 90, .5)


# #recording
import time
import pypot.robot


from pypot.primitive.move import MoveRecorder, Move, MovePlayer

# robot.m1.goal_position = 40
# robot.m2.goal_position = 10
# robot.m3.goal_position = 10
# time.sleep(2)
# print(robot.m1.present_position)

#feed in robot, framerate, motors
# move_recorder = MoveRecorder(robot, 70, robot.motors)
# #make motors compliant
# robot.compliant = True
# #record for 10 seconds
# print("RECORD")
# move_recorder.start()
# time.sleep(7)
# move_recorder.stop()
# print("STOPPING")
#
# time.sleep(2)
# # playback
# with open('trial1.move', 'w') as f:
#     move_recorder.move.save(f)
# print("PLAYING")
#
# with open('trial1.move') as f:
#     m = Move.load(f)
#
#
# robot.compliant = False
#
# move_player = MovePlayer(robot, m)
# #starting playback, sleep for duration of playback otherwise you will get a thread issue
# move_player.start()
# time.sleep(7)
# print("PLAYED")
