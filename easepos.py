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
from easing import *
import math

import pypot.robot

robot = pypot.robot.from_config(spyder_config)

# Put the robot in its initial position
for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.moving_speed = 40
    # m.goal_position = 0


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


        time.sleep(0.01)



# Wait for the robot to actually reach the base position.
time.sleep(2)
# pos = 0

motionalert1= [
    [robot.m1, easeInOutQuart, robot.m1.present_position, -60] ,
    [robot.m2 ,easeInOutQuart, robot.m2.present_position, 20.3] ,
    [robot.m3 ,easeInOutQuart, robot.m3.present_position, 20]]

motionalert2= [
    [robot.m1, easeInOutQuart, robot.m1.present_position, 60] ,
    [robot.m2 ,easeInOutQuart, robot.m2.present_position, 20.3] ,
    [robot.m3 ,easeInOutQuart, robot.m3.present_position, 20]]

motionforward= [
    [robot.m1, easeInOutQuart, robot.m1.present_position, 0] ,
    [robot.m2 ,easeInOutQuart, robot.m2.present_position, 45] ,
    [robot.m3 ,easeInOutQuart, robot.m3.present_position, 58]]


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

        time.sleep(0.01)


# robot.m1.goal_position = -50
robot.m2.goal_position = 40
robot.m3.goal_position = -6
print("Rest")

time.sleep(3)

easingMultiple(motionalert1, 3)

time.sleep(1)

easingMultiple(motionalert2, 2)

time.sleep(1)

easingMultiple(motionforward, 2)

# printer.println("Hello World")
# printer.feed(5)

time.sleep(.1)

# robot.m1.goal_position = -50
robot.m2.goal_position = 40
robot.m3.goal_position = -6
print("Rest")

time.sleep(3)
