a = [9, 2, 8, 6, 4]
# 2 9 8 6 4
# 2 4 8 6 9
def select(a):
	for i in range(len(a)):
		min_index = i
		for j in range(i+1, len(a)):
			if a[min_index] > a[j]:
				min_index = j
		a[min_index], a[i] = a[i], a[min_index]
	return a

print(select(a))
