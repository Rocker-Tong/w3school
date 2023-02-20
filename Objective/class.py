class Student(object):
    count = 0

    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender
        Student.count += 1

    def __del__(self):
        Student.count -= 1

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_gender(self):
        return self.__gender

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('wrong gender')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if not isinstance(self.__score, int):
            return 'Please input a valid number'
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


#############################################
#        Inheritance and Polymorphism       #
#############################################
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


class Timer(object):
    pass


def run_twice(animal):
    animal.run()
    animal.run()


#############################################
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x
