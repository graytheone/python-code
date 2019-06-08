#利用列表生成式表达该for循环
a = [1, 2, 3, 4, 5, 6]
r = []

for i in range(len(a)-1):
	r.append(a[i]*10+a[i+1])

print(r)



r = [a[i]*10+a[i+1] for i in range(len(a)-1)]
print(r)
