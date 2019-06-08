#1.输入一个3位整数，判断它是否为水仙花数。当输入数据不正确时，要求给出错误提示。说明：水仙花数是一位3位数，其各位数的立方之和等于该数本身，如153=1**3+5**3+3**3。

num = 153

xx = int( num / 100 )
yy = int( (num / 10) % 10 )
zz = int( num % 10 )

x = input()
y = input()
z = input()
a = 100*x + y*10 + z
int(a)
for x in range(1,10):
	for y in range(1,10):
		for z in range(1,10):
			if x**3 + y**3 + z**3 == a:
				print(a)
			else:
				print('You are wrong')
				

