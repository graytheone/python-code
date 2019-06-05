#1. how to express 20 < x < 30 in Python
x < 30 and x > 20
#2. if: a = 0, b = 3, c = 4, what is the result of (a&b|c)
a = 0000 b = 0011 c = 0100
(a&b|c) = (0000 | 0100) = (0100)
#3. if: a = 0, b = 3, c = 4, what is the result of (~a&b>c)
a = 0000 b = 0011 c = 0100
(~a&b>c) = (0011 | 0100 ) = False
#4. write an expression which can be divisible by 3 and 7 at the same time

def a(x):
	if x > 0:
		x = int(x)
	return(True)

a(21)



