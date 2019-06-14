
def my_abs(a):
	if a > 0:
		return a
	if a < 0:
		return -a
	


a = [10, -11, 2, -5]
print(sorted(a, key = my_abs))
