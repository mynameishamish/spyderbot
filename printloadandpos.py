spyder_config = {
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
import os
from tempsensing import temp

import pypot.robot

amp = 30
freq = 0.5

robot = pypot.robot.from_config(spyder_config)


# Wait for the robot to actually reach the base position.

t = threading.Timer(.5, temp)
t.start()

while True:

    m1pos = robot.m1.present_position
    m2pos = robot.m2.present_position
    m3pos = robot.m3.present_position
    m1load = robot.m1.present_load
    m2load = robot.m2.present_load
    m3load = robot.m3.present_load

    if m1pos is not None and m1load is not None:
        # print('m1Pos={0:0.1f} m2Pos={1:0.1f} m3Pos={2:0.1f}'.format(m1pos, m2pos, m3pos))
        print('m1Load={0:0.1f} m2Load={1:0.1f} m3Load={2:0.1f}'.format(m1load, m2load, m3load))

    time.sleep(.1)
