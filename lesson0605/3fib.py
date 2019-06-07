#.without list
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a+b
		n = n+1
	return 'done'

#2.with list
a = [0, 1]
def fib1(max):
	n = 0
	while n+1 < max:
		a.append(a[n]+a[n+1])
		print(a)
		n = n+1
	return 'done'

fib1(5)
