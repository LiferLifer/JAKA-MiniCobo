import math
import time
import __common

def main():
    robot_IP = "192.168.200.100"
    rc = jkrc.RC(robot_IP)
    print(rc.login())
    print(rc.power_on())
    print(rc.enable_robot())

    while True:
        ret = rc.get_tcp_position()
        if not ret[0]:
            print("get_tcp_pos ok & tcp pos is: {}".format(ret[1]))
        else:
            print("get_tcp_pos failed.")

if __name__ == '__main__':
    __common.init_env()
    import jkrc
    main()