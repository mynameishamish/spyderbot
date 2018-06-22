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
import copy
import pypot
import pypot.robot
robot = pypot.robot.from_config(spyder_config)


        # raise NotImplementedError
x = easeInOutSine
y = easeOutBack
linear = linearTween
s = easeInExpo
eib = easeInBack
eoc = easeOutCirc


x = easeInOutSine
y = easeOutBack
linear = linearTween
s = easeInExpo
eib = easeInBack
eoc = easeOutCirc
eoq = easeOutQuint
eoe = easeOutExpo
eie = easeInExpo

motionrest= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -77] ,
    [robot.m3 , x, robot.m3.present_position, 73]]

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




# motions

motionofferNew= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , y, robot.m2.present_position, -45] ,
    [robot.m3 , y, robot.m3.present_position, 110]]

motionNodup = [
    [robot.m3 , linear, robot.m3.present_position, 120]]

motionNoddown = [
    [robot.m3 , linear, robot.m3.present_position, 100]]

motionAfteroffer = [
    # [robot.m1 , x, robot.m1.present_position, robot.m1.present_position] ,
    [robot.m2 , y, robot.m2.present_position, -60] ,
    [robot.m3 , y, robot.m3.present_position, 130]]

midpos = [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -65] ,
    [robot.m3 , x, robot.m3.present_position, 130]
]

turnaway = [
    [robot.m1 , x, robot.m1.present_position, 57.5] ,
    [robot.m2 , x, robot.m2.present_position, -32.5] ,
    [robot.m3 , x, robot.m3.present_position, 103.5]
]

listen = [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -75] ,
    [robot.m3 , x, robot.m3.present_position, 107]
]

strench  = [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , s, robot.m2.present_position, -57] ,
    [robot.m3 , x, robot.m3.present_position, 140]
]

look = [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , eib, robot.m2.present_position, -53] ,
    [robot.m3 , x, robot.m3.present_position, 143]
]

read = [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -35] ,
    [robot.m3 , x, robot.m3.present_position, 114]
]

musicdown = [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , eoc, robot.m2.present_position, -65] ,
    [robot.m3 , x, robot.m3.present_position, 75]
]

musicup = [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , eoc, robot.m2.present_position, -55] ,
    [robot.m3 , x, robot.m3.present_position, 99]
]

# sigh, perform best when the speed is 45, 45, 45
turn1 = [
    [robot.m1 , x, robot.m1.present_position, -55] ,
    [robot.m2 , x, robot.m2.present_position, -45] ,
    [robot.m3 , x, robot.m3.present_position, 100]
]

turnup = [
    [robot.m1 , x, -55, -55] ,
    [robot.m2 , x, -45, -53] ,
    [robot.m3 , x, 100, 117]

]

turndown = [
    [robot.m1 , x, -55, -55] ,
    [robot.m2 , x, -53, -50] ,
    [robot.m3 , x, 117, 98]
]

#check from different angle, perform best when the speed is 45, 45, 45
check1 = [
    [robot.m1 , s, robot.m1.present_position, -46] ,
    [robot.m2 , s, robot.m2.present_position, -67] ,
    [robot.m3 , y, robot.m3.present_position, 83]

]

check2 = [
    [robot.m1 , s, robot.m1.present_position, 35] ,
    [robot.m2 , s, robot.m2.present_position, -67] ,
    [robot.m3 , s, robot.m3.present_position, 83]

]



def overheating():
    speeds=[]
    motors=robot.motors
    if max([m.present_temperature for m in motors])>=71:
        speeds=[m.present_speed for m in motors]


        print("motors are overheating")
        console.log("motors are overheating")
        print("going to limp rest")
        resting()
        limp()

        while True:
            inp=raw_input("for current temps press t and hit enter \nto re-engage motors type m:")
            if inp=="t":
                print([(m.name, m.present_temperature) for m in motors])
            if inp=="m":
                print("re-engageing motors")
                livly([200,40,40])
                break
            else:
                print("invalid input")

def easing(motor, e_fn, final_position, duration):
    motor.moving_speed=200
    t0=time.time()
    d= duration
    b= motor.present_position
    c=final_position-b

    while True:
        t=float(time.time()-t0)
        if t>=d:
            break
        pos =e_fn(t, b, c, d)
        y= pos
        motor.goal_position=pos
        time.sleep(0.00001)


def easingMultiple(motions, duration):
    println(motions)
    println(duration)
    robot.m1.moving_speed = 200
    robot.m2.moving_speed = 200
    robot.m3.moving_speed = 200
    t0=time.time()
    d= duration
    change=[m[3]-m[0].present_position for m in motions]
    start=[int(m[0].present_position) for m in motions]
    motion=[m[:2]+[start.pop(0)]+[change.pop(0)] for m in motions]
    while True:
        t=float(time.time()-t0)
        if t>=d:
            break
        for m in motion:
            fn= m[1]
            pos =fn(t, m[2], m[3], d)
            y=pos
            m[0].goal_position=pos
            time.sleep(0.00001)



# Position definitions, just pass in moving_speed for each motor

def resting(z=30, x=30, c=30):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -4
    robot.m2.goal_position = -77
    robot.m3.goal_position = 73
    time.sleep(2)
    print("Rest")
    # printer.println("Rest")
    # printer.feed(3)

def alert(z=30, x=30, c=30):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -4
    robot.m2.goal_position = -65
    robot.m3.goal_position = 135
    print("Alert")
    time.sleep(2)

def forward(z=30, x=30, c=30):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -4
    robot.m2.goal_position = -45
    robot.m3.goal_position = 149
    print("Forward")
    time.sleep(2)

def offer(z=30, x=30, c=30):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -4
    robot.m2.goal_position = -26
    robot.m3.goal_position = 112
    print("Offer")
    time.sleep(2)

def blocking(m1=robot.m1.present_position, m2=robot.m1.present_position, m3=robot.m1.present_position, m1speed=30, m2speed=30, m3speed=30):
    robot.m1.moving_speed = m1speed
    robot.m2.moving_speed = m2speed
    robot.m3.moving_speed = m3speed
    robot.m1.goal_position = m1
    robot.m2.goal_position = m2
    robot.m3.goal_position = m3
    time.sleep(2)

def concur():
    nodup=[
    [robot.m2, easeInQuart, robot.m2.present_position, -55],
    [robot.m3, easeInQuart, robot.m3.present_position, 140]
    ]

    noddown1=[
    [robot.m2, easeInQuart, robot.m2.present_position, -65],
    [robot.m3, easeInQuart, robot.m3.present_position, 135]
    ]

    print("down")
    easingMultiple(noddown1, 1)
    # time.sleep(.05)
    print("up")
    easingMultiple(nodup, 1 )

# def nod():
motionNodup = [
    [robot.m3 , linear, robot.m3.present_position, 120]]

motionNoddown = [
    [robot.m3 , linear, robot.m3.present_position, 100]]

ParticipantRight= [
    [robot.m1 , x, robot.m1.present_position, -45] ,
    [robot.m2 , eie, robot.m2.present_position, -52] ,
    [robot.m3 , eoq, robot.m3.present_position, 105]]
ParticipantLeft= [
    [robot.m1 , x, robot.m1.present_position, 37] ,
    [robot.m2 , eie, robot.m2.present_position, -52] ,
    [robot.m3 , eoq, robot.m3.present_position, 105]]

ParticipantCenter= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , eie, robot.m2.present_position, -52] ,
    [robot.m3 , eoq, robot.m3.present_position, 105]]

leftpos = [
    [robot.m1 , x, robot.m1.present_position, 25] ,
]
rightpos = [
    [robot.m1 , x, robot.m1.present_position, -35] ,
]
midpos = [
    [robot.m1 , x, robot.m1.present_position, -4] ,
]
def shake():
    easingMultiple(rightpos, .5)
    easingMultiple(leftpos, .5)
    time.sleep(.05)
    easingMultiple(midpos, .35)
    # easingMultiple(leftpos, .45)
    # time.sleep(.05)
    print("up")

    # easingMultiple(midpos, 1)


def nod():
    print("down")
    easingMultiple(motionNoddown, .5)
    time.sleep(.05)
    print("up")
    easingMultiple(motionNodup,.5)

def sigh():
    easingMultiple(turn1,1.5)
    time.sleep(1)
    print("up")
    easingMultiple(turnup,1.5)
    print("down")
    easingMultiple(turndown,1.5)
    time.sleep(1)

def checkaround():
     easingMultiple(look,1)
     time.sleep(0.5)
     # easingMultiple(motionrest,1)
     # time.sleep(1)
     easingMultiple(check1,1)
     time.sleep(1)
     easingMultiple(check2,1.5)
     time.sleep(2)

def limp():
    print("returning home")
    easingMultiple(motionrest, 1)
    time.sleep(2)
    print("compliant")

    for m in robot.motors:
        m.compliant = True
    time.sleep(1)

def livly(speeds):
    print("returning home")
    easingMultiple(motionrest, 1)
    time.sleep(2)
    print("not compliant")

    for m, s in zip(robot.motors, speeds):
        m.compliant = False
        m.set_moving_speed = s
    time.sleep(2)
def offer():
    easingMultiple(motionoffer, 1.5)

def alertmotion():
    easingMultiple(motionalert, 1.5)
