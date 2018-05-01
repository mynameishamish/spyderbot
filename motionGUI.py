import time
import math
import numpy

from easing import *
from motions import *

from tkinter import *
 
x = easeInOutSine
y = easeOutBack
linear = linearTween
s = easeInExpo
eib = easeInBack
eoc = easeOutCirc
eoq = easeOutQuint
eoe = easeOutExpo
eie = easeInExpo

# motions

# print("starting Easepos")

motionrest= [
    [robot.m1 , x, robot.m1.present_position, -4] ,
    [robot.m2 , x, robot.m2.present_position, -77],
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

ScreenLeft= [
    [robot.m1 , x, robot.m1.present_position, 22] ,
    [robot.m2 , eie, robot.m2.present_position, -45] ,
    [robot.m3 , eie, robot.m3.present_position, 132]]
ScreenRight= [
    [robot.m1 , x, robot.m1.present_position, -30] ,
    [robot.m2 , eie, robot.m2.present_position, -45] ,
    [robot.m3 , eie, robot.m3.present_position, 132]]
ParticipantRight= [
    [robot.m1 , x, robot.m1.present_position, -45] ,
    [robot.m2 , eie, robot.m2.present_position, -52] ,
    [robot.m3 , eoq, robot.m3.present_position, 105]]
ParticipantLeft= [
    [robot.m1 , x, robot.m1.present_position, 37] ,
    [robot.m2 , eie, robot.m2.present_position, -52] ,
    [robot.m3 , eoq, robot.m3.present_position, 105]]
# resting(30,30,30)

# time.sleep(2)



window = Tk()
 
window.title("Spyderbot Motion")
 
window.geometry('400x350')
 
# lbl = Label(window, text="Hello")
 
# lbl.grid(column=0, row=0)
 
def checkleftscreen():
     print("Check Left Screen")
     easingMultiple(ScreenLeft, 1.2)
def checkrightscreen():
     print("Check Right Screen")
     easingMultiple(ScreenRight, 1.2)
def checkLeftParticipant():
     print("Check Left Participant")
     easingMultiple(ParticipantLeft, 1.2)
def checkRightParticipant():
     print("Check Right Participant")
     easingMultiple(ParticipantRight, 1.2)
def rest():
	print("rest")
	easingMultiple(motionrest,1)


LeftScreen = Button(window, text="Check Left Screen", command=checkleftscreen)
LeftScreen.grid(column=0, row=0)

RightScreen = Button(window, text="Check Right Screen", command=checkrightscreen)
RightScreen.grid(column=2, row=0)

LeftParticipant = Button(window, text="Check Left Participant", command=checkLeftParticipant)
LeftParticipant.grid(column=0, row=2)

RightParticipant = Button(window, text="Check Right Participant", command=checkRightParticipant)
RightParticipant.grid(column=2, row=2)

rest = Button(window, text = "rest", command = rest)
rest.grid(column=5,row = 4)


window.mainloop()




