# 要求：3个一组读取字符，显示在屏幕上，每读一次休息1秒钟。
import time
with open(r"test.txt", "r") as f:
    strChar = f.read(3)
    while strChar:

        print(strChar)
        time.sleep(1)
        strChar = f.read(3)
