import multiprocessing
import time

def clock(f):
    while True:
        print("now time is:{0}".format(time.ctime()))
        time.sleep(f)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(3,))
    p.start()
    p.join()
    