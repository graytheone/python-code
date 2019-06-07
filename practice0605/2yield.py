#利用yield生成range(20)每次将数打印出来

#def my_range(num):
#	pass

#for x in my_range(20):
#	print(x)

def my_range(num):
	for x in my_range(20):
		print(x)
		yield 20
