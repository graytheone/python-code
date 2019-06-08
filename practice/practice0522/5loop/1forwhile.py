#1.输入0-100之间奇数总和

x = 0
sums = 0
for x in range(0,101):
	if x %2 == 1:
		sums = sums + x 
		print(sums)


