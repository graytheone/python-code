#output the list [1*2, 3*4, 5*6, 7*8, ... ,99*100]
x = 1
L = [ x*(x+1) for x in range(1,101) if x%2 != 0 ]
#L = [ x for x in range(1,101) and x%2 != 0]


a = []
for x in range(1, 101):
	if x%2 != 0:
		a.append(x*(x+1))

#L = [x*(x+1) for x in range(1, 100) and x%2 != 0]
print(L)


