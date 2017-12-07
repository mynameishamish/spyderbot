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

amp = 30
freq = 0.5

robot = pypot.robot.from_config(spyder_config)

# Put the robot in its initial position
for m in robot.motors: # Note that we always provide an alias for all motors.
    m.compliant = False
    # m.goal_position = 0

# Wait for the robot to actually reach the base position.
time.sleep(2)
# pos = 0

# print(robot.m1.present_position)
# robot.m1.goal_position = pos
# time.sleep(.02)
# print(robot.m1.present_position)


# # Do the sinusoidal motions for 10 seconds
# t0 = time.time()

# while True:
#     t = time.time() - t0

#     if t > 10:
#         break

#     pos = amp * numpy.sin(2 * numpy.pi * freq * t)

#     robot.m1.goal_position = pos


#     time.sleep(0.02)
def easeInQuad(t):
    return t**2

def easeInOutBack(t, s=1.70158):
    t *= 2
    if t < 1:
        s *= 1.525
        return 0.5 * (t * t * ((s + 1) * t - s))
    else:
        t -= 2
        s *= 1.525
        return 0.5 * (t * t * ((s + 1) * t + s) + 2)

def easing(motor, e_fn, final_position, duration):

    t0=time.time()
    while True:
        present_pos= motor.present_position
        if present_pos>=final_position:
            break
        t_current=time.time()-t0
        pos =e_fn(t_current)
        motor.goal_position=pos
        print(present_pos)

        time.sleep(0.02)

easing(robot.m1, easeInOutBack, 90, 2)
