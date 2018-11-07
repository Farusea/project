import random
L = []
for k in range(100): # 将下面语句执行100次，也就是随机生成一个有100位数的列表
    i = random.randint(0, 99)
    L.append(i)
print(L)
L1 = sorted(L) # 将随机列表按升序排列（sorted与sort不一样，这种排序方法可降序）
print(L1)