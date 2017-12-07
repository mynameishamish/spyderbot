import pypot.robot

spider_robot = pypot.robot.from_config(spider_robot_config)

for m in spider_robot.base:
    print(m.present_position)
