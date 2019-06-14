from functools import reduce
if __name__ == '__main__':
	n = input()
	num = [int(n[i]) for i in range(0, len(n))]
	summ = reduce(lambda x, y: x+y, num)
	maps = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu'}
	summ = str(summ)
	i = 0
	for i in range(0, len(summ)-1):
		print(maps[summ[i]], end = ' ')
	if i == 0:
		i = 0
	else:
		i = i+1
	print(maps[summ[i]])
	exit(0)
