# 装饰器（Decrator）在不改动函数代码的基础上无限制扩展函数功能的一种机制

import time
# 高阶函数，以函数作为参数。
def printTime(f):# 装饰器有特定的写法。
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)
    return wrapper

# 装饰器必须写在函数的前面
@printTime # "@"是python里面的语法糖
def Time():
    print("上面是现在的时间，哈哈哈！")

Time()

