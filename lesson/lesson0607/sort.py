a = [9, 2, 8, 6, 4]

mins = a[0]
for i in range(1,len(a)):
	if a[i]< mins:
		mins = a[i]
print(mins)
a[0],a[1] = a[1],a[0]
#2 9 8 6 4

mins = a[1]
pos = 1
for i in range(2,len(a)):
	if a[i] < mins:
		mins = a[i]
		pos = i
print(mins)
a[1], a[pos] = a[pos], a[1]

#2 4 8 6 9

mins = a[2]
pos = 2
for i in range(3,len(a)):
	if a[i] < mins:
	mins = a[i]
	pos = i
print(mins)
a[2],a[pos] = a[pos],a[2]

