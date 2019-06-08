#实现以下fibonacci数列，均使用函数def，并且测试调用，查看结果是否正确。

#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#1.借用list存储元素



#2.不借用list,直接交换元素,将每次的值print出来



#3.借用yield, 使用调用yield,下一次执行函数不从头开始,而是从上次返回yield处继续执行
#(hint:yield的作用相当于return)
temp = [0, 1]

def fib():
	for i in range(2, 10):
		temp.append(a[i-1]+a[i-2])

def fib():
	a = 1, b = 1
	for i in range(10):
		c = a+b
		print(c)
		a = b
		b = c
	


x = []
def fib(i):
	i,a,b = 0,0,1
	for i in range(10):
		print(b)
		a,b = b,a+b
		x.append(b)
	return('finish')

def fib(i):
	i,a,b = 0,0,1
	for i in range(10):
		print(b)
		a,b=b,a+b
	
	return('finish')

def fib(i):
	i,a,b=0,0,1
	for i range(10):
		yield(b)
		a,b=b,a+b
	return('finish')		
	
