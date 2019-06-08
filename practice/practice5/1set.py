#remove repeated elements in list

import random
a = [ random.randint(1, 5) for x in range(1, 10)]

print('before:{}'.format(a))
b = set(a)

print('after:{}'.format(b))

