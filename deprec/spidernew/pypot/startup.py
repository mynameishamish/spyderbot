from pypot.robot.config import spider_robot_config

my_config = dict(spider_robot_config)
my_config['controllers']['my_dxl_controller']['port']  = 'auto'
