#利用列表生成式实现下列for循环实现的功能

a = 'abc'
b = '123'

for x in a:
	for y in b:
		print(x+y)




r = [x + y for x in a for y in b]
print(r)
