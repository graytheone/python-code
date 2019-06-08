#use both for-loop and while-loop to program
#1.从键盘输入k, 输出1**2+2**2+3**2+4**2...+k**2的结果
#k = input('please enter a number')
#k = int(k)
#sums = 0
#for x in range(1,k+1):
	#sums = x**2 + sums
	#print(sums)


k = input('please enter a number')
k = int(k)
sums = 0
x = 0
while x <= k:
	x = x + 1    
	sums = x**2 + sums
	print(sums)



