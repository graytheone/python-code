
if __name__ == '__main__':
	
	n = input()
	n = int(n)
	t = 1
	while n != 1:
		if n % 2 != 0:
			n = (3*n + 1)//2
		if n % 2 == 0:
			n = n//2
		t = t + 1

	print(t)
	

	
	
	
