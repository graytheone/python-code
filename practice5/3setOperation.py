a = set('abcef123456')
b = set('adfg123789')

#union
a|b
#intersection
a&b
#difference
a-b
#symmetric_difference
a-(a&b)
b-(a&b)
a-(a&b) | b-(a&b)
