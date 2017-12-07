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
            'angle_limit': [-70.0, 70.0],
            'offset': 0.0
        },
        'm2': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 3,
            'angle_limit': [20.3, 50.0],
            'offset': 0.0
        },
        'm3': {
            'orientation': 'direct',
            'type': 'AX-12A', 'id': 4,
            'angle_limit': [-6.0, 62.0],
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
    m.compliant = False
    m.moving_speed = 40
    # m.goal_position = 0

# Wait for the robot to actually reach the base position.
# pos = 0


# Position definitions, just pass in moving_speed for each motor

def rest(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = 0
    robot.m2.goal_position = 20.3
    robot.m3.goal_position = -6
    print("Rest");

def alert(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = -70
    robot.m2.goal_position = 15.5
    robot.m3.goal_position = 23.3
    print("Alert");


def up(z, x, c):
    robot.m1.moving_speed = z
    robot.m2.moving_speed = x
    robot.m3.moving_speed = c
    robot.m1.goal_position = 70
    robot.m2.goal_position = 50
    robot.m3.goal_position = 62
    print("Up")
