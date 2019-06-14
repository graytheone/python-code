L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(L):	
	L = sorted(L, key = lambda item:item[0])
	print(L)

by_name(L)
