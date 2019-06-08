a = [9, 2, 8, 6, 4]
#2 9 8 6 4
#2 8 9 6 4
#2 8 6 9 4
#2 8 6 4 9

#2 8 6 4 9
#2 6 8 4 9
#2 6 4 8 9
#2 4 6 8 9

#
def bubble(a):
	for i in range(len(a)):
		for j in range(0, len(a)-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	return a

print(bubble(a))




