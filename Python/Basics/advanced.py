# Slice
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


# Iterate
def findMinAndMax(list):
    if not list:
        return None, None
    # Min
    mini = maxi = list[-1]
    for elem in list:
        if elem < mini:
            mini = elem
        elif elem > maxi:
            maxi = elem
    return mini, maxi


# List comprehensions ***生成器***
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]


# Fibonacci
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]


n = 0
for t in triangles():
    print(t)
    n += 1
    if n > 5:
        break


# A generator that can represent the whole set of the natural numbers
def nature():
    n = 0
    while True:
        n += 1
        yield n

