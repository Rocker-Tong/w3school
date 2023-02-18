def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


# ==============================================================
# Closure
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x = 0

    def counter():
        nonlocal x
        x += 1
        return x

    return counter


# 装饰器 (Decorator)：在代码运行期间动态增加功能的方式
import functools, time

"""def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper"""


def log(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text:
                print('%s %s():' % (text, func.__name__))
            else:
                print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2023-2-18')


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args, **kwargs)
    return fn

