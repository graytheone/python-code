a = [1,1]
for x in range(2,10):
	c = a[x - 1]
	b = a[x - 2]
	e = c + b
	a.append(e)
print(a)




a1 = 1
a2 = 2
for x in range(5):
	a3 = a1 + a2
	a1 = a2
	a2 = a3
#	print(a3)


def fib(a1,a2):
	for x in range(5):
		a3 = a1 + a2
		a1 = a2
		a2 = a3
		print(a3)


print(fib(1,2))
	
