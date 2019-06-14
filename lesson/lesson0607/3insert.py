a = [9, 2, 8, 6, 4]
temp = []
# temp = [2, 8, 9]

def insert(a):
	insert_pos = 0
	for i in range(len(a)):
		for j in range(len(temp)):
			insert_pos = j
			if temp[j] > a[i]:
				break;
		temp.insert(insert_pos, a[i])

insert(a)
print(temp)
