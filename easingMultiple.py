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
import easing
import pypot.robot
import math

amp = 30
freq = 0.5

robot = pypot.robot.from_config(spyder_config)

# Put the robot in its initial position
for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False




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

#motion syntax
#motion = [[motor, function, motor.present_position, final_position]]
#example motion
motion1= [[robot.m1, easeInOutQuad, robot.m1.present_position, 100] , [robot.m2 ,easeInOutSine, robot.m2.present_position, 100]]
motion2= [[robot.m1, easeInOutQuad, robot.m1.present_position, 200] , [robot.m2 ,easeInOutSine, robot.m2.present_position, 200]]

def easingMultiple(motion, duration):
    t0=time.time()
    d= duration
    for m in motion:
        m[3]= m[3]-m[2]
    while True:
        t=float(time.time()-t0)
        if t>=d:
            break
        for m in motion:
            fn= m[1]
            pos = fn(t, m[2], m[3], d)
            m[0].goal_position=pos

        time.sleep(0.02)

# robot.m1.goal_position = 0
# robot.m2.goal_position = 0
#
time.sleep(2)

robot.m1.moving_speed = 20
robot.m2.moving_speed = 20
robot.m3.moving_speed = 20

robot.m1.goal_position = 62
robot.m2.goal_position = 176
robot.m3.goal_position = 179

time.sleep(10)

# easingMultiple(motion1, 2)

time.sleep(2)
