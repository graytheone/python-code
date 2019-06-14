#判断一个数是不是素数

#函数返回true OR false
#def isPrime(x):
#	pass


#输入一个数
#x = input(x)
#x = int(x)

#print(isPrime(x))




x = input('>')
x = int(x)
def isPrime(x):
	if x > 1:
		for i in range(2,x):
			if x%i == 0:
				return 0 
		return 1
	else:
		return 1
	

print(isPrime(x))


