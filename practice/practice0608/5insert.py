a = [8, -3, 5, 2, -1, 100, 2]


b = []
def insert_sort(a):
	position = 0
	for x in range(len(a)):
		for y in range(len(b)):
			positions = y
			if b[y] < a[x]:
				b.insert(positions , a[i])

print(b) 
