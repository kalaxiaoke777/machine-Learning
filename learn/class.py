a = [1,2]
b = [1,4]
a.append(b)
b.append(a)
del a
# del b
print(b)