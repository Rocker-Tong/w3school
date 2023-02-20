class Student(object):
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    # __slots__ = ('name', 'age')
    def __init__(self):
        self._score = 0

    # @property 可以把一个方法变成属性调用

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2023 - self._birth


# The use of @property
class Screen(object):
    def __init__(self):
        pass

    # __len__方法：能让class作用于len()函数
    def __len__(self):
        return self._width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        # 错误判断
        if not isinstance(value, int):
            raise ValueError('Must be an integer')
        if value <= 0:
            raise ValueError('Invalid value')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be an integer')
        if value <= 0:
            raise ValueError('Invalid value')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


class Fib(object):
    def __init__(self) -> None:
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b

        if self.a > 100000:
            raise StopIteration
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# 枚举类
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


class Gender(Enum):
    Male = 0
    Female = 1


class Student1(object):
    def __init__(self, name, gender) -> None:
        self.name = name
        if not isinstance(gender, Enum):
            raise TypeError('Gender type error')
        self._gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if not isinstance(value, Enum):
            raise TypeError('Gender type error')
        self._gender = value

# Metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass