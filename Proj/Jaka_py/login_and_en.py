import __common

def main():
    robot_IP = "192.168.200.100"
    try:
        rc = jkrc.RC(robot_IP)
        rc.login()
        rc.enable_robot()
        # rc.logout()
    except Exception as e:
        print("Exception: {}".format(e))
        

if __name__ == '__main__':
    __common.init_env()
    import jkrc
    main()