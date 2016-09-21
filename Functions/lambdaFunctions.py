import functools

sum = lambda arg1, arg2: arg1 + arg2

#print(sum(1, 2))

vals = range(100)
r = map(lambda v: v % 2, vals)
rr = filter(lambda v: v % 2 == 0, vals)

# for i in r: print(i, end=' ')
# print('\n')
# for i in rr: print(i, end=' ')

rrr = functools.reduce(lambda a, x: a + x, vals)
print(rrr)