a = [0, -5, 28, 10, -2, 8, 5]
#-5 0 28 10 -2 8 5
#-5 0 10 28 -2 8 5
#-5 0 10 -2 28 8 5
#-5 0 10 -2 8 28 5
#-5 0 10 -2 8 5 28
#=5 0 -2 10 8 5 28

def bubble_sort(a):
	for x in range(len(a)):
		for y in range(0,len(a)-1-x):
			if a[y] > a[y+1]:
				a[y] , a[y+1] = a[y+1] , a[y]
				
				
	return a 

print(bubble_sort(a))
