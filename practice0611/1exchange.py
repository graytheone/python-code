#输入三个数x, y, z, 把这三个数由小到大输出

#def fun(x, y, z):
#	pass


#输入三个数
#x = input()
#y = input()
#z = input()

#调用函数
#fun(int(x), int(y), int(y))


x = input('>')	
y = input('>')
z = input('>')
x = int()
y = int()
z = int()
#listt = [x , y ,z]

def fun(x,y,z):
	lisst = [x, y, z]
	return sorted(listt)

print(sorted(listt , key = fun))
