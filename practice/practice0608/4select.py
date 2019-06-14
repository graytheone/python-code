import random

a = [random.randint(-100, 100) for i in range(1, 30)]
print(a)


def select_sort(a):
	for x in range(1,30):
		mins index = x
		for y in range(1+x , 30):
			if a[mins_index] > a[y]:
				a[mins_index],a[y] = a[y],a[mins_index]
	return a

print(select_sort(a))
