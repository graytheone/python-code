#实现以下fibonacci数列，均使用函数def，并且测试调用，查看结果是否正确。

#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#1.借用list存储元素



#2.不借用list,直接交换元素,将每次的值print出来



#3.借用yield, 使用调用yield,下一次执行函数不从头开始,而是从上次返回yield处继续执行
#(hint:yield的作用相当于return)

a = []
def fib(i):
	i,a,b = 0,0,1
	for i in range(10):
		print(b)
		a,b = b,a+b
		a.append(b)

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
	
