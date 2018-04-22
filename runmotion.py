
# everything beside dance has been fix. Won't cause moter over heated right now. Dance will be updated soon. 
import time
import math
import numpy

from easing import *
from motions import *

#easing 
x = easeInOutSine
y = easeOutBack
linear = linearTween
s = easeInExpo
eib = easeInBack
eoc = easeOutCirc

# motions

print("starting Easepos")

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
    [robot.m3 , x, robot.m3.present_position, 140]]

motionoffer= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -15] ,
    [robot.m3 , x, robot.m3.present_position, 112]]


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
resting(30,30,30)

time.sleep(2)

#run motions!
while True: 
    print('Choose a motion:')
    command = input()
    if command == "offer":
        print("offer")
        easingMultiple(motionofferNew, 1.5)
    elif command == "nod":
        print("nod")
        easingMultiple(motionNodup, 1)
        easingMultiple(motionNoddown, 1)
    elif command == "midpos":
        print("midpos")
        easingMultiple(midpos,1)
    elif command == "listen":     
        easingMultiple(listen,1)
    elif command == "turnaway":
        easingMultiple(turnaway,1)
    elif command == "awake":
        easingMultiple(strench,2)
        time.sleep(1)
        easingMultiple(listen,1)
    elif command == "look":
        easingMultiple(look,1)
    elif command == "read":
        easingMultiple(read, 1)
    elif command == "dance":
        while True:
            easingMultiple(musicdown,1)
            easingMultiple(musicup,1)
            time.sleep(0.2)
            n = input()
            if n == "break":
                break
    elif command == "rest":
        easingMultiple(motionrest, 1.5)
    elif command == "break":
        print("rest")
        easingMultiple(motionrest, 1.5)
        break

