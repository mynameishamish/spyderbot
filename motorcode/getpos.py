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
            'type': 'AX-12A', 'id': 1,
            'angle_limit': [-90.0, 90.0],
            'offset': 0.0
        },
        'm2': {
            'orientation': 'direct',
            'type': 'AX-18A', 'id': 2,
            'angle_limit': [4.0, 50.0],
            'offset': 0.0
        },
        'm3': {
            'orientation': 'direct',
            'type': 'AX-18A', 'id': 3,
            'angle_limit': [0.0, 38.0],
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

# Put the robot in its initial position
for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = True

    # m.goal_position = 0

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
