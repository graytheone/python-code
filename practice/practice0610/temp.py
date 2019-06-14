a = [0, 4, 8, 16, 20, 24, 28, 32, 36]

#1.how many times it takes to find the element 4 and the element 20



#2.def binary_search(): and trying to return the times it take to find a element

def binary_search(a, item):
	low = 0 
	high = len(a) - 1
	count = 0

	while low < high:
		mid = (low + high)//2
		guess = a[mid]
		count = count + 1
		if guess == item:
			return count
		if guess < item:
			low = mid+1
		if guess > item:
			high = mid-1
	return None

print(binary_search(a, 4))
