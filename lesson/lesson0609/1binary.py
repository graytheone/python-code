import random

def binary(a, data):
	low = 0
	high = len(a)-1
	while low <= high:
		mid = (low+high) // 2
		if a[mid] > data:
			high = mid-1
		elif a[mid] < data:
			low = mid+1
		else:
			return mid
	return -1

a = [random.randint(-10, 10) for i in range(1, 20)]
a.sort()
print(a)
print(binary(a, 5));

