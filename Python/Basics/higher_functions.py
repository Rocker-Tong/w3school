# Higher-order function
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收**两个**参数，
# reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        # map接收Iterable，所以可以将输入的string转换为单个char进行逐个char to num操作
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# =========================================================
# 使用lambda函数进一步简化
def char2num1(s):
    return DIGITS[s]


def str2int1(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num1, s))


# 首字母大写，其他小写
def normalize(name):
    return name[0].upper() + name[1:].lower()


def prod(L):
    def mul(x, y):
        return x * y
    return reduce(mul, L)


# =========================================================
# String to float
def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    s1, s2 = s.split('.')[0], s.split('.')[-1]
    return reduce(fn, map(char2num, s1)) + \
        reduce(fn, map(char2num, s2)) * 10 ** -len(s2)


def str2float1(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)


def is_odd(n):
    return n % 2 == 1


def not_empty(s):
    return s and s.strip()


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始数列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


# =========================================================
# 回数
def is_palindrome(n):
    s = str(n)
    return s[::-1] == s


def is_palindrome1(n):
    s = str(n)
    return ''.join(reversed(s)) == s


# =========================================================
# sorted()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return -t[1]

