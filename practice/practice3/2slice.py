a = 'abcdefghijklmnopqrstuvwxyz'

#1.output a certain string with only odd index
for x in range(0,26):
	if x%2 != 0:
		print(a[x], end = ' ')
#2.output a certain string with only even index
for x in range(0,26):
	if x%2 == 0:
		print(a[x])
#3.output 'xyzabc'
print(a[-4:-1]+a[0:3])
#4.output the last five character in the string
print(a[-6:-1])
#5.output the rest string after the character 'e'
a[5:]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1.output a certain list with only odd index
#two ways:(1).slice (2).for+if
#(1).
[b[x] for x in range(0,10) if x%2 != 0]
[x for x in b if x % 2 != 0]

#(2).
for x in range(0,10):
	if x%2!=0 :
		print(a[x], end=' ')


#2.output a certain list with only even index
#two ways:(1).slice (2).for+if
#(1).

#(2).for x in range(0,10):
	if x%2 == 0:
		print(a[x])
