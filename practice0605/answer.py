student = ['student%d'%i for i in range(16) if i > 0]
print(student)

a = [1, 2, 3, 4, 5, 6, 7]
b = [a[x]*10+a[x+1] for x in range(len(a)-1)]
print(b)

a = 'abc'
b = '123'
l = [x+y for x in a for y in b]
print(l)
