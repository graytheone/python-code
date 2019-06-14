#输出9*9乘法口诀表
#代码填空，在____填入相应的代码

def multiply():
	for i in range(1, 10):
		print('\n')
		for j in range(1, i+1):
			print('%d * %d = %d' % (i, j, i*j), end = ' ')

#函数调用
multiply()
