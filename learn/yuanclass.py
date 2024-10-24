from functools import reduce

f = lambda x, y: x/y

asd = reduce(f, range(1, 11))

print(asd)