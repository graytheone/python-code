
#BMI index
#--------------------------
# index     | ???
#--------------------------
# [0, 18.5) | underweight
# [18.5,25) | normal
# [25, 28)  | overweight
# [28, 32)  | obesity
# [32, +∞)  | severe obesity
#---------------------------
#
#input any BMI index and output the result 

x = 23
if x >= 0 and x<18.5:
	print('underweight')
elif x >=18.5 and x<25:
	print('normal')
elif x >= 25 and x<28:
	print('overweight')
elif x >= 28 and x<32:
	print('obesity')
else:
	print('severe obesity')


 
