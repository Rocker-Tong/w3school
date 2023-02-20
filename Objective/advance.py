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
