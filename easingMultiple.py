#motion syntax
#motion = [[motor, function, motor.present_position, final_position]]
#example motion
motion1= [[robot.m1, easeInOutQuad, robot.m1.present_position, 44] , [robot.m2 ,easeInOutSine, robot.m2.present_position, 44]]

def easingMultiple(motion, duration):
    t0=time.time()
    d= duration
    for m in motion:
        m[3]= m[3]-m[2]
    while True:
        t=float(time.time()-t0)
        if t>=d:
            break
        for m in motion:
            fn= m[1]
            pos = fn(t, m[2], m[3], d)
            m[0].goal_position=pos

        time.sleep(0.02)