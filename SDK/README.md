# JAKA_MiniCobo-SDK



（开发商提供）**SDK/JAKA_SDK资料包V2.1.1_R(1)** 下部分文档简要介绍：

- 1.doc：主要包括C/C++/C#/Python四种语言二次开发文档，以及C/C++/C#动态库dll调用方法；
- 2.linux：包含一些已经写好的linux下的demo；
- 3.windows：包含一些已经写好的windows下的demo；
- 4.readme：官方提供资源附带的readme；
- 5.微软常用运行库合集：一些WINDOWS下的编译依赖环境；



（JAKA官网提供）**SDK/SDK** 下部分文档简要介绍：

- c：C语言二次开发文档；
- c#：C#语言二次开发文档；
- c++：C++四种语言二次开发文档；
- jaka_ROS：机械臂ROS开发相关文档；
- JAKA_TCP资料：JAKA机械臂TCP底层通信机制相关文档；
- python：Python语言二次开发文档。



### README Official

|---SDK2.1.4            内含主要发布内容动态库文件及头文件
     |---linux
          |---c&c++          适用于c&c++的dll
               |---i686-linux-gnu       由该linux编译器编译的dll
               |---x86_64-linux-gnu     由该linux编译器编译的dll
               |---aarch64-linux-gnu    由该linux编译器编译的dll
          |---python3        适用于python的dll
               |---i686-linux-gnu        由该linux编译器编译的dll
               |---x86_64-linux-gnu      由该linux编译器编译的dll
     |---window
          |---c&c++          适用于c&c++的dll
               |---x86          32位编译的dll
               |---x64          64位编译的dll
          |---python3        适用于python的dll
               |---x86          32位编译的dll
               |---x64          64位编译的dll
     |---example 部分功能示例
|---doc                      二次开发说明文档及调用指南         



使用须知：
windows平台使用sdk前需要安装微软常用运行库合集.exe



**V2.1.3--------->V2.1.4更新说明:**
修复：

1. 修复 c++ joint_move_extend 圆弧转接无法使用的问题。
2. 修复ftp存在upload后偶尔不能download的问题。
3. 修复函数is_in_pos返回true, 但是运动不到位的问题(适配RC1.5.13.8之后的版本，
RC1.7.0.45之后的版本，RC1.7.1.7之后的版本)。
4. 修复与外部使用相同库，导致函数名称冲突的问题。
5. 修复C代码中handler分配策略,修复多次create,destory导致handler不唯一的问题。
6. 修复get_tcp_position在断网状态下未正确返回错误码的问题。
7. 修复c#、c、c++ Modbus模拟浮点数输出为整数的问题。

废止:
1. 停止支持运行.ngc的脚本程序。



**V2.1.2--------->V2.1.3更新说明:**
修复：
1.python:get_robot_status中添加末端按钮状态部分。
2.登出后is_net_connect仍然为1的问题。
3.修复C# set_admit_ctrl_config 失败的问题。
4.修复python SDK连接多台机器人失败的问题。
新增：
1.圆弧运动添加设定圈数的功能。



**V2.1.1--------->V2.1.2更新说明:**
修复：
1.控制器断电后，启动控制器使用SDK第一次上电引发的数据异常
2.直线运动沿y轴阻塞失效。
3.屏蔽info级控制器错误信息，该信息在app中为绿色。
4.修复状态函数与指令函数竞争端口导致收发异常。
5.适配1.7版本的io，改变robot_status的IO部分结构。
6.适配1.5.13.09之后的机器人状态信息。
新增：
1.支持设置阻塞运动超时时间
2.新增获取DH参数接口
3.新增状态末端tio_key的值，控制器1.5.13.20或1.7版本及以上可用
4.新增设置与获取工具力控传感器的低通滤波截止频率，控制器1.7版本可用
5.新增设置与获取工具力控传感器的限位参数，控制器1.7版本可用
6.新增设置与获取工具末端电压，控制器1.7版本可用
7.get_robot_status 接口新增监测瞬时速度和瞬时力矩
8.win平台下运行SDK时，将会生成日志到当前用户的Temp目录下



**V2.0.1--------->V2.1.1更新说明:**
修复：
1.修复偶发的program读取失败问题。
2.修复极差网络环境下，偶现阻塞运动部分情况下失效的问题，需要同步控制器版本至1.5.13.09
3.修复C语言和python语言在不进行logout的情况下再次login导致内存占用增加的bug
4.修复program_load()加载程序不支持中文的bug
5.修复extio状态显示和is_extio_running失效的问题，需要更新控制器至1.5.13.x
6.修复自动重连机制造成的logout之后仍能通过对应类或描述符控制机器人运动。
7.修复python语言在机器人描述符释放时出现段错误的问题
8.修复app和控制器联合调试时，SDK小概率获取不到错误码的问题，需要同步控制器版本至1.5.13.09
9.修复日志在logout方法调用之后不再记录。
新增：
1.添加tcp坐标系下沿着坐标轴相对运动功能，需要同步控制器版本至1.5.13.09
2.新增FTP接口，支持对轨迹和app程序的上传下载，需要同步控制器版本至1.5.13.x



### Reference

1 . 节卡MinoCobo机器人单目视觉抓取的ROS实现：https://blog.csdn.net/woniu_12345/article/details/122511503