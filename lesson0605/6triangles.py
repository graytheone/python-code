def triangles():
	L = [1]
	n = 0
	yield L
	while n < 10:
		L = [1] + [L[x]+L[x+1] for x in range(len(L)-1)] + [1]
		n = n+1
		yield L

n = 0
for L in triangles():
	print(L)
#f = triangles()
#print(next(f))
#print(next(f))	


a = [1,2,3,4]
b =( 10**(len(a)))*a[0]
for x in range(len(a)):
	b = a[x] * (10**(len(a)-x))

from functools import reduce
def fn(x,y):
	return x*10 + y
reduce(fn,[1,2,3,5,7,9])
