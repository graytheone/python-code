import random

a = [random.randint(-100, 100) for i in range(1, 30)]
print(a)

b = []

def insert_sort():
	positions = 0
	for x in range(1,30):
		for y in range(len(b)):
			positions = y
			if b(positions) < a[x]:
				b.insert(positions,a[x])
print(b)

