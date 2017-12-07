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

from Adafruit_Thermal import *
printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=99999999)
printer.begin()
printer.feed(2)


amp = 30
freq = 0.5
robot = pypot.robot.from_config(spyder_config)


# Go to rest positions
robot.m1.moving_speed = 20
robot.m2.moving_speed = 20
robot.m3.moving_speed = 20
robot.m1.goal_position = 0
robot.m2.goal_position = 20.3
robot.m3.goal_position = -6

# Position definitions, just pass in moving_speed for each motor

def resting(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = 0
    robot.m2.goal_position = 20.3
    robot.m3.goal_position = -6
    time.sleep(2)
    print("Rest")
    printer.println("Rest")
    printer.feed(3)

def alert(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -70
    robot.m2.goal_position = 18.5
    robot.m3.goal_position = 23.3
    print("Alert")

def up(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = 70
    robot.m2.goal_position = 50
    robot.m3.goal_position = 62
    print("Up")


resting(20, 20, 20)

time.sleep(2)
