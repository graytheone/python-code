#不借助list编写fibonacci数列

#输出含有n个数的fibonacci数列
#def fabonacci(n):
	#pass

#输入
#n = input()
#n = int()

#1 1 2 3 5 8 13 ...
#函数调用
#fabonacci(n)
n = input('>')
n = int()
def fabonacci(n):
	a = 0
	b = 1
	for i in range(0, n + 1):
		if i <= n:
			
			a, b = b, a+b
			i = i + 1
	return 'done'
		

print(fabonacci(n))	
