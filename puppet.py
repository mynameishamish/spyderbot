# import pypot.dynamixel
# import time
#
# puppet_robot = {
#     'controllers': {
#         'my_dxl_controller': {
#             'sync_read': False,
#             'attached_motors': ['robot1', 'robot2'],
#             'port': 'auto'
#         }
#     },
#     'motorgroups': {
#         'robot1': ['m2','m1'],
#         'robot2': ['m4']
#     },
#     'motors': {
#         'm1': {
#             'orientation': 'direct',
#             'type': 'AX-12A',
#             'id': 1,
#             'angle_limit': [-90.0, 90.0],
#             'offset': 0.0
#         },
#         'm2': {
#             'orientation': 'direct',
#             'type': 'AX-12A',
#             'id': 4,
#             'angle_limit': [-90.0, 90.0],
#             'offset': 0.0
#         },
#         'm4': {
#             'orientation': 'direct',
#             'type': 'AX-12A',
#             'id': 2,
#             'angle_limit': [-90.0, 90.0],
#             'offset': 0.0
#         }
#     }
# }
#
# import pypot.robot
# robot = pypot.robot.from_config(puppet_robot)
#
#
# while True:
#     robot.m1.goal_position = 0
#     robot.m2.goal_position = 0
#     robot.m4.goal_position = 0
#
#     time.sleep(1)
#     print(robot.m1.present_position)
#     print(robot.m2.present_position)
#     print(robot.m4.present_position)
#
#     robot.m1.goal_position = 50
#     robot.m2.goal_position = 50
#     robot.m4.goal_position = 50
#
#     time.sleep(1)


puppet_config = {
    'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['robot1', 'robot2'],
            'port': 'auto'
        }
    },
    'motorgroups': {
        'robot1': ['m1', 'm2', 'm3'],
        'robot2': ['m4', 'm5', 'm6']
    },
    'motors': {
        'm1': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 4,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm2': {
            'orientation': 'direct',
            'type': 'AX-18A', 'id': 5,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm3': {
            'orientation': 'direct',
            'type': 'AX-18A', 'id': 6,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm4': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 1,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm5': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 2,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm6': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 3,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
    }
}
import time
import numpy
import threading
from easing import *
import math
import copy
import pypot
import os
import pypot.robot
robot = pypot.robot.from_config(puppet_config)
# from tempsensing import *
import time
import threading
# from motions import *
from Adafruit_IO import Client, Feed

timeout = 6

ADAFRUIT_IO_KEY = os.environ.get('adafruit_io_key')
ADAFRUIT_IO_USERNAME = 'mynameishamish'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

m1temp_feed = aio.feeds('spyderbot.base')
m2temp_feed = aio.feeds('spyderbot.neck')
m3temp_feed = aio.feeds('spyderbot.head')

def temp():
    while True:
        # print("temp")
        m1temp = robot.m1.present_temperature
        m2temp = robot.m2.present_temperature
        m3temp = robot.m3.present_temperature
        if m1temp is not None and m2temp is not None:
            print('m1Temp={0:0.1f}*C m2Temp={1:0.1f}*C m3Temp={2:0.1f}*C'.format(m1temp, m2temp, m3temp))
            # Send humidity and temperature feeds to Adafruit IO
            m1temp = '%.2f'%(m1temp)
            m2temp = '%.2f'%(m2temp)
            m3temp = '%.2f'%(m3temp)

            aio.send(m1temp_feed.key, str(m1temp))
            aio.send(m2temp_feed.key, str(m2temp))
            aio.send(m3temp_feed.key, str(m3temp))
        # else:
        #     print('Failed to get DHT22 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')
        # Timeout to avoid flooding Adafruit IO
        time.sleep(timeout)


# t = threading.Timer(.5, temp)
# t.start()
#
# while True:
#     print("loop")
#     time.sleep(1)

for m in robot.motors:
    m.set_moving_speed = 50
    m.compliant = False

robot.m1.goal_position = 0
robot.m2.goal_position = -42
robot.m3.goal_position = -21

robot.m4.goal_position = 0
robot.m5.goal_position = -42
robot.m6.goal_position = -21

time.sleep(1)

for m in robot.motors:
    m.set_moving_speed = 200


robot.m4.compliant = True
robot.m5.compliant = True
robot.m6.compliant = True

robot.m1.compliant = False
robot.m2.compliant = False
robot.m3.compliant = False

for m in robot.motors:
    m.set_moving_speed = 5

# robot.m2.goto_position = robot.m1.present_position
robot.m1.goal_position = robot.m4.present_position
robot.m2.goal_position = robot.m5.present_position
robot.m3.goal_position = robot.m6.present_position

time.sleep(1)

t = threading.Timer(.5, temp)
t.start()

while True:
    for m in robot.motors:
        m.set_moving_speed = 200
    # # robot.m1.goal_position = 0
    # robot.m2.goal_position = 0
    # robot.m4.goal_position = 0
    # print(robot.m1.present_position)
    # print(robot.m2.present_position)
    # print(robot.m4.present_position)
    # time.sleep(1)
    # # robot.m1.goal_position = 50
    # robot.m2.goal_position = 50
    # robot.m4.goal_position = 50
    # print(robot.m1.present_position)
    # time.sleep(1)

    # robot.m2.goto_position(10, 1., wait=True)
    # robot.m2.goal_position = robot.m1.present_position
    robot.m1.goal_position = robot.m4.present_position
    robot.m2.goal_position = robot.m5.present_position
    robot.m3.goal_position = robot.m6.present_position
    time.sleep(.0001)
