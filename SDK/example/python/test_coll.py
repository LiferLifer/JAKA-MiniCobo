import __common
import time

def main():
    robot_IP = "192.168.200.100"
    try:
        # 
        rc = jkrc.RC(robot_IP)

        # rc.login()
        # rc.power_on()
        # rc.enable_robot()
        # ret = rc.get_collision_level()
        # print(ret)
        # rc.set_collision_level(1)
        ret = rc.get_collision_level()
        print(ret)
        num = 0
        while(1):
            ret = rc.is_in_collision()
            collision_status = ret[1]
            if collision_status == 1:
                time.sleep(5)
                rc.collision_recover()
                print(" in collision "+ str(num))
            else:
                print("the robot is not in collision "+ str(num))
                time.sleep(1)
            num=num+1

        rc.logout()
    except Exception as e:
        print("Exception: {}".format(e))

if __name__ == '__main__':
    __common.init_env()
    import jkrc
    main()
