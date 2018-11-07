import time
import threading
import datetime

def f1(a):
    print("第一个线程开始运行的时间:", time.ctime())
    time.sleep(4)
    print("这是参数:", a)
    print("第一个线程结束的时间:", time.ctime())

def f2(a, b):
    print("第二个线程开始运行的时间:", time.ctime())
    time.sleep(2)
    print("这是参数:", a, "和参数", b)
    print("第二个线程结束的时间:", time.ctime())

def main():
    starttime = datetime.datetime.now()
    print("此进程开始的时间:", time.ctime())
    t1 = threading.Thread(target= f1, args=("one", ))
    t1.start()
    t2 = threading.Thread(target= f2, args=("two", "three"))
    t2.start()

    t1.join()
    t2.join()
    print("此进程结束的时间:", time.ctime())
    endtime = datetime.datetime.now()
    print("该程序总共运行了{0}秒".format(endtime-starttime))


if __name__ == '__main__':  # 直接调用主函数
    main()

# 多线程通用包：treading
# 格式为：t = treading.Tread(target=xxx. args=(xxx,))
#         t.setdaemon(Ture)守护线程-daemon
#         t.start() 启动多线程
#         t.join()  等待多线程完毕
