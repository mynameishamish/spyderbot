spyder_config = {
    'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['base'],
            'port': 'auto'
        }
    },
    'motorgroups': {
        'base': ['m1', 'm2', 'm3'],
    },
    'motors': {
        'm1': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 3,
            'angle_limit': [-48.0, 40.0],
            'offset': 0.0
        },
        'm2': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 5,
            'angle_limit': [-77.0, -42.0],
            'offset': 0.0
        },
        'm3': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 6,
            'angle_limit': [85.0, 149.0],
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

x = easeInOutSine


# Put the robot in its initial position
for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.moving_speed = 40
    # m.goal_position = 0


motionrest= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -77] ,
    [robot.m3 , x, robot.m3.present_position, 85]]

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


# Position definitions, just pass in moving_speed for each motor

def resting(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -4
    robot.m2.goal_position = -77
    robot.m3.goal_position = 85
    time.sleep(2)
    print("Rest")
    # printer.println("Rest")
    # printer.feed(3)

def alert(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -4
    robot.m2.goal_position = -65
    robot.m3.goal_position = 135
    print("Alert")
    time.sleep(2)

def forward(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -4
    robot.m2.goal_position = -45
    robot.m3.goal_position = 149
    print("Forward")
    time.sleep(2)

def offer(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -4
    robot.m2.goal_position = -26
    robot.m3.goal_position = 112
    print("Offer")
    time.sleep(2)

def blocking(m1, m2, m3, m1speed=30, m2speed=30, m3speed=30):
    robot.m1.moving_speed = m1speed
    robot.m2.moving_speed = m2speed
    robot.m3.moving_speed = m3speed
    robot.m1.goal_position = m1
    robot.m2.goal_position = m2
    robot.m3.goal_position = m3
    time.sleep(2)


