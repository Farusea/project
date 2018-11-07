import threading
sum = 0
loopSum = 10000
lock = threading.Lock()
def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()
        sum += 1
        lock.release()


def myJian():
    global sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()
        sum -= 1
        lock.release()

def main():
    print('start--{}'.format(sum))
    t1 = threading.Thread(target=myAdd, args=( ))
    t2 = threading.Thread(target=myJian, args=( ))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('end--{}'.format(sum))

if __name__ == '__main__':
    main()

# 真的搞不懂，明明一模一样的代码，运行出来居然不一样！！！！！！！！！！！！卖了疯冷！