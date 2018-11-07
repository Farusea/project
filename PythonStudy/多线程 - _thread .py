import time
import _thread as thread
import datetime  # 本来想用来统计程序运行的时间的,但是这个程序的包_thread有缺陷

def f1():
    print("第一个线程开始运行的时间:", time.ctime())
    time.sleep(4)
    print("第一个线程结束的时间:", time.ctime())

def f2():
    print("第二个线程开始运行的时间:", time.ctime())
    time.sleep(2)
    print("第二个线程结束的时间:", time.ctime())

def main():
    print("此进程开始的时间:", time.ctime())
    thread.start_new_thread(f1, ())
    thread.start_new_thread(f2, ())
 #   f1()  # 非线程按照程序的顺序执行
 #   f2()
    print("次进程结束的时间:", time.ctime())


if __name__ == '__main__':  # 直接调用主函数
    main()
    while True:  # 一个死循环，可以让主函数永远不停止
        time.sleep(1)

