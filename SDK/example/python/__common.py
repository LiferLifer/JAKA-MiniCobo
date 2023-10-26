import os
import sys
import ctypes
import platform

__system = platform.system()

if __system == "Windows":
    print("Windows!")
    def init_env():
        print("No Windows SDK, please use Linux SDK.")

elif __system == "Linux":
    print("Linux!")
    def init_env():
        # Linux 需要将 libjakaAPI.so 和 jkrc.so 放在同一个文件夹下，并添加当前文件夹路径到环境变量
        # .bashrc: export LD_LIBRARY_PATH=/xx/xx/

        lib_path = os.getenv("LD_LIBRARY_PATH")
        if lib_path is None:
            print("Please set LD_LIBRARY_PATH in .bashrc")
            sys.exit(0)
        else:
            path_libjakaAPI = lib_path + "/libjakaAPI.so"
            path_jkrc = lib_path + "/jkrc.so"
            if not os.path.exists(path_libjakaAPI):
                print("libjakaAPI.so not exist.")
                sys.exit(0)
            if not os.path.exists(path_jkrc):
                print("jkrc.so not exist.")
                sys.exit(0)
            try:
                sys.path.append(lib_path)
                ctypes.CDLL(path_libjakaAPI)
                ctypes.CDLL(path_jkrc)
            except Exception as e:
                print("Load so failed: {}".format(e))
                sys.exit(0)

else:
    print("what's this?")


if __name__ == '__main__':
    init_env()
