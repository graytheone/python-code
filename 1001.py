

if __name__ == '__main__':
	n = input()
	n = int(n)
	count = 0
	while n != 1:
		count = count + 1
		if n % 2 == 0:
			n = n // 2
		else:
			n = (3*n+1)//2
	print(count)

		
