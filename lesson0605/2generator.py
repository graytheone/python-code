l = [x*x for x in range(11)]

g = (x*x for x in range(11))

print(l)

print(g)
#how to iterator the generator
#next(g)
for i in g:
	print(i)

