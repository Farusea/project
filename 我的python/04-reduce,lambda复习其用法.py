from functools import reduce
# help(reduce)
n = int(input("input a number:"))
f = reduce(lambda x, y: x*y, [i for i in range(1,n+1)])
print("{0}的阶乘是{1}".format(n, f))