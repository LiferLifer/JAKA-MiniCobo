import math
import time
import __common

def main():
    jstep_pos = [0, 0, 0, 0, 5 / 180.0 * math.pi, 0]
    jstep_neg = [0, 0, 0, 0, -5 / 180.0 * math.pi, 0]

    robot_IP = "192.168.200.100"
    rc = jkrc.RC(robot_IP)
    
    print(rc.login())
    print(rc.power_on())
    print(rc.enable_robot())

    while True:
        print('joint_move {}'.format(rc.joint_move(jstep_pos, 0, True, 2 * math.pi)))
        time.sleep(5)
        print('joint_move {}'.format(rc.joint_move(jstep_neg, 0, True, 2 * math.pi)))
        time.sleep(5)

if __name__ == '__main__':
    __common.init_env()
    import jkrc
    main()

    