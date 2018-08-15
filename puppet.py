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
            'type': 'AX-12A', 'id': 1,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm2': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 2,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm3': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 3,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm4': {
            'orientation': 'direct',
            'type': 'AX-18A', 'id': 4,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm5': {
            'orientation': 'direct',
            'type': 'AX-18A', 'id': 5,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
        'm6': {
            'orientation': 'direct',
            'type': 'AX-18A', 'id': 6,
            'angle_limit': [-180.0, 180.0],
            'offset': 0.0
        },
    }
}
import time
import numpy
from easing import *
import math
import copy
import pypot
import pypot.robot
robot = pypot.robot.from_config(puppet_config)

robot.m1.compliant = True
robot.m2.compliant = True
robot.m3.compliant = True
robot.m4.compliant = False

for m in robot.motors:
    m.set_moving_speed = 20

# robot.m2.goto_position = robot.m1.present_position
robot.m4.goto_position = robot.m1.present_position
robot.m5.goal_position = robot.m2.present_position
robot.m6.goal_position = robot.m3.present_position

time.sleep(2)


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
    robot.m4.goal_position = robot.m1.present_position
    robot.m5.goal_position = robot.m2.present_position
    robot.m6.goal_position = robot.m3.present_position
    time.sleep(.0001)
