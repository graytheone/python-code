#1.从键盘输入3个整数的到变量a, b, c中，将这三个数由小到大进行排序，使a中存放最小数，c中存放最大数，然后依次输出a, b, c
x = input('please enter an inter')
y = input('please enter an inter')
z = input('please enter an inter')
x = int(x)
y = int(y)
z = int(z)
if (x < y ) and (x < z) and (y < z):
	a = x
	b = y
	c = z
	print(a,b,c)
elif y < x < z:
	a = y
	b = x
	c = z
	print(a,b,c)
elif z < y < x:
	a = z
	b = y
	c = x
	print(a,b,c)
else:
	print(y,z,x)


