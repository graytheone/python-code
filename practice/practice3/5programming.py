#1.determine if there is a number 10 in the list
#(hint: using the given list a)
import random
a = []
for i in range(10):
	a.append(random.randint(1, 10))
print(a)
for x in a:
	if x == 10:
		print(x)
y = [x for x in a if x == 10]
#2.input a year and judge whether a year is a leap year
#(hint: leap year means (1).year%4 == 0 and year%100 != 0 (2).year%400 == 0
year = input()
int(year)	
if year%4 == 0 and year%100 != 0 or year%400 == 0:
	print('leap year')
else:
	print('normal year')

