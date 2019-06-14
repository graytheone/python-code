a = 1
b = 2

def abc():
	a = 10

def change(c, d):
#	self.a, self.b = self.b, self.a
	a, b = b, a
	print(a, b)

def change_list(a):
	a[0] = 100
	
if __name__ == '__main__':
#	a = 5
#	b = 10
#	change(a, b)
	c = [1, 3, 4]
	change_list(c)
	print(c)
