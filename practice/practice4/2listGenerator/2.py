#output all the values which can be divided by 3
a = list(range(0, 100))

l = [ x for x in range(0, 100) if a[x]%3 == 0]
l1 = [ x for x in a if x%3 == 0]

#output all the valuse whose index can be divided by 3
l = [x for x in range(0,100) if x % 3 == 0]
print('l')
