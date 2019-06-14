a = [-2, 5, -3, 72, -9, 22, 1]

def select_sort(a):
	for x in range(len(a)):
		mins_index = x
		for y in range(x+1,len(a)):
			if a[mins_index] > a[y]:
				a[mins_index],a[y] = a[y],a[mins_index]
	return a

print(select_sort(a))
