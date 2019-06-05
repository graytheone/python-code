#1.编写程序，输入三角形的3条边长，求其面积。注意：三角形的任意两边之和必须大于第三边，对于不合理边长的输入，要求给出错误提示。

x = input('>')
y = input('>')
z = input('>')
x = int(x)
y = int(x)
z = int(y)
if (x + y > z) and ( x + z >y ) and (y + z > x):
	a =( x + y + z)/2
	area =(a*(a-x)*(a-y)*(a-z))**0.5
	print(area)
else:
	print('you are wrong')








