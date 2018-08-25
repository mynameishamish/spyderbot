spyder_config = {
    'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['robot1'],
            'port': 'auto'
        }
    },
    'motorgroups': {
        'robot1': ['m1', 'm2', 'm3']
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
        }
    }
}
import time
import numpy

import pypot.robot

amp = 30
freq = 0.5

robot = pypot.robot.from_config(spyder_config)

robot.m1.compliant = True
robot.m2.compliant = True
robot.m3.compliant = True



# Wait for the robot to actually reach the base position.


time.sleep(2)
print("Motor 1 is at position: ", robot.m1.present_position)
print("Motor 2 is at position: ", robot.m2.present_position)
print("Motor 3 is at position: ", robot.m3.present_position)


time.sleep(5)
print("Motor 1 is at position: ", robot.m1.present_position)
print("Motor 2 is at position: ", robot.m2.present_position)
print("Motor 3 is at position: ", robot.m3.present_position)

time.sleep(5)
print("Motor 1 is at position: ", robot.m1.present_position)
print("Motor 2 is at position: ", robot.m2.present_position)
print("Motor 3 is at position: ", robot.m3.present_position)

time.sleep(5)
