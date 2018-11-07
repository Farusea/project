import time
import random
import threading
# 选择排序
def selectSort(myList):
	starttime = time.time()
	length = len(myList)
	for i in range(0, length-1):
		min = i
		for j in range(i+1, length):
			if myList[i]>myList[j]:
				myList[i], myList[j] = myList[j], myList[i]
	print("选择排序后：{0}".format(myList))
	endtime = time.time()
	print("选择排序耗时：{0}秒".format(endtime-starttime))

# 插入排序
def insretSort(myList):
	starttime = time.time()
	length = len(myList)
	for i in range(1, length):
		if myList[i-1] > myList[i]:
			temp = myList[i]
			index = i
			while index > 0 and myList[index-1] > temp:
				myList[index] = myList[index-1]
				index -= 1
			myList[index] = temp
	print("插入排序后：{0}".format(myList))
	endtime = time.time()
	print("插入排序耗时：{0}秒".format(endtime-starttime))

# 希尔排序
def shellSort(myList):
	starttime = time.time()
	step = int(len(myList)/2)
	while step > 0:
		for i in range(step, len(myList)):
			temp = myList[i]
			j = i
			while j >= step and temp < myList[j-step]:
				myList[j] = myList[j - step]
				j -= step
			myList[j] = temp
		step = int(step/2)
	print("希尔排序后：{0}".format(myList))
	endtime = time.time()
	print("希尔排序耗时：{0}秒".format(endtime-starttime))

# 快速排序
def quickSort(myList, left, right):

	if left >= right:
		return
	mid = myList[left]
	low, high = left, right
	while low < high:
		while low < high and myList[high] >= mid:
			high -= 1
		myList[low] = myList[high]
		while low < high and myList[low] < mid:
			low += 1
		myList[high] = myList[low]
	myList[low] = mid
	quickSort(myList, left, low-1)
	quickSort(myList, low+1, right)

def main():
# 产生一个0-29999的随机列表，列表长度为20000且列表里的数字不重复
	L = random.sample(range(0, 30000), 20000)
	print("初始列表为：{0}".format(L))
	print("-"*150)
	starttime = time.time()
	quickSort(L, 0, len(L)-1)
	endtime = time.time()
	print("快速排序后：{0}".format(L))
	print("快速排序耗时：{0}秒".format(endtime - starttime))
	t1 = threading.Thread(target=selectSort, args=(L, ))
	t1.start()
	t2 = threading.Thread(target=insretSort, args=(L, ))
	t2.start()
	t3 = threading.Thread(target=shellSort, args=(L, ))
	t3.start()


	t1.join()
	t2.join()
	t3.join()



if __name__ == '__main__':
	main()


