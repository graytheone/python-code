#将下列for循环功能用列表生成式实现
#1.
student = []

for i in range(1, 15):
	student.append('student%d'%i)

print(student)



student = []

r = ['student%d'%i for i in range(1,15)]
print(r)
