# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# SOME USEFUL THINGS
# ======================
print()

# ternary operation
n = 10
status = 'odd' if n % 2 else 'even'
print(status)

# zip
a = [2, 3, 4]
b = [5, 6, 7]
c = [8, 9, 0]
d = ['a', 'b', 'c']
print(dict(zip(d, [a, b, c])))

# filter
n = [11, 12, 33, 43, 55, 66, 76, 88]

def odd(x):
    return x % 2
b = filter(odd, n)
print(list(filter(odd, n)))
print(type(b))


# map
def remainder(x):
    return x % 10
print(list(map(remainder, n)))


# reduce
from functools import reduce

def mult(a, b):
    return a*b
print(reduce(mult, n))


# string joins
l = ['a', 'cdf', 'di', 'gre']
print('-'.join(l).replace('-','%'))

# string translation
s = 'hello world!!'
t = {'l': '8', 'o': '7'}
s1 = 'lo'
s2 = '87'
table = s.maketrans(s1, s2, '!') # creates a translation table
print(s.translate(table))


print()