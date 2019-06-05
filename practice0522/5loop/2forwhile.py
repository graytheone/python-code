#1.从键盘输入k的值以及k个整数，统计其中正数，零和负数的个数
		
k = input('please input a number k')
k = int(k)
x = 0
listt = list

while len(listt) == k :
	x = input('please enter k numbers')
	x = int(x)
	listt.append(x)
	
print(listt)

for i in range(0,k+1):
	if listt[i] == 0:
		print('These numbers are zero')
		len(listt.remove[i])
	elif listt[i] < 0:
		print('These numbers are negative numbers')
		len(listt.remove[i])	
	else:
		print('These numbers are positive numbers')
		len(listt.remove[i])
