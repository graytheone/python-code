import random

a = [random.randint(-10, 100) for i in range(1, 30)]
print(a)




def bubble_sort(a):
	for x in range(1,30):
		for y in range(1,(29-x)):
			if a[y] < a[y+1]:
				a[y] , a[y+1] = a[y+1] , a[y]
	return(a)

bubble_sort(a)
