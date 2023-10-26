import math
import time
import __common

def main():

    robot_IP = "192.168.200.100"
    rc = jkrc.RC(robot_IP)

    while True:
        print("===================")

        print('login: {}'.format(rc.login()))
        print('power_on: {}'.format(rc.power_on()))
        print('enable_robot: {}'.format(rc.enable_robot()))

        print('disable_robot: {}'.format(rc.disable_robot()))
        print('power_off: {}'.format(rc.power_off()))
        print('logout: {}'.format(rc.logout()))

        print()


if __name__ == '__main__':
    __common.init_env()
    import jkrc
    main()