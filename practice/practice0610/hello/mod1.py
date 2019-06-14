import sys

def test():

	args = sys.argv
	if len(args) == 1:
		print(args[0])
	elif len(args) == 2:
		print(args[1])
	else:
		print('Too many')

if __name__ == '__main__':
	test()
