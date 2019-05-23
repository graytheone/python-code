a = set('abcef123456')
b = set('adfg123789')

#union
u1 = a | b
u2 = a.union(b)
#print(u1)

#intersection
i1 = a & b
i2 = [ x for x in a if x in b]
i3 = a.intersection(b)
#print(i3)

#difference
d1 = [x for x in a if x not in b]
d2 = a.difference(b)
d3 = b.difference(a)

#symmetric_difference
temp1 = a-b
temp2 = b-a
s1 = set(temp1|temp2)
s2 = a^b
print()

