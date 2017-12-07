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
# import motions

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=99999999)
printer.begin()
printer.feed(-5)


amp = 30
freq = 0.5

robot = pypot.robot.from_config(spyder_config)

# Put the robot in its initial position
for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    m.moving_speed = 20
    # m.goal_position = 0

# Wait for the robot to actually reach the base position.
time.sleep(2)
# pos = 0

robot.m1.goal_position = 0
robot.m2.goal_position = 20.3
robot.m3.goal_position = 0

time.sleep(3)
