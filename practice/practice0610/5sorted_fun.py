a = [-10, 0, 2, -5, 12, 4]

#1.sorted with 2*a[x]
#(hint: use def fun(): & key = fun))



def fun(x):
	return 2*a[x]

sorted(a,key = fun)
