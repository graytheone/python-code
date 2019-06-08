#实现下列函数功能：找到列表中最大的数

a = [1, 23, 4, 5, 6, 2, 3, 100, 3, 23, 3123, 2]

def find_max_element(a):
	maxs = a[0]
	for i in range(1,len(a)):
		if a[i] > maxs:
			maxs = a[i]
	return maxs

def find_min_element(a):
	mins = a[0]:
	for i in range(1,len(a)):
		if a[i] < mins:
			mins = a[i]
	return mins			


print(find_max_element(a))
#预期输出结果：3123
