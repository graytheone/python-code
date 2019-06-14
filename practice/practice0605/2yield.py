#利用yield生成range(20)每次将数打印出来

#def my_range(num):
#	pass

#for x in my_range(20):
#	print(x)

def my_range(num):
	for i in range(20):
		num = num+1
	return num

print(my_range(0))

for i in my_range(0):
	print(i)

next(my_range(0))
