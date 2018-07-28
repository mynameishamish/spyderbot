import pypot.dynamixel
import time

ports = pypot.dynamixel.get_available_ports()

if not ports:
    raise IOError('no port found!')

print('ports found', ports)

print('connecting on the first available port:', ports[0])
dxl_io = pypot.dynamixel.DxlIO(ports[0])

time.sleep(.5)

print(dxl_io.scan(range(10)))

time.sleep(.5)

dxl_io.set_goal_position({1: 25})
dxl_io.set_goal_position({2: 25})
dxl_io.set_goal_position({4: 25})

time.sleep(.5)

dxl_io.set_goal_position({1: 15})
dxl_io.set_goal_position({2: 15})
dxl_io.set_goal_position({4: 15})
