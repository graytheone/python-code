#*
#***
#*****
#*******


for x in range(4):
	for y in range(7):
		if (x == 0 and y >= 1) or  (x ==1 and y>= 3) or (x == 2 and y>= 6):			print(' ',end = ' ')
		else:
			print('*',end = ' ')
	print('\n')
