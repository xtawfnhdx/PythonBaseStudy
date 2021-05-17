class Animals(object):
    __slots__ = ('a', 'b', 'c')

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 'c'


class Cat(Animals):
    __slots__ = ("name")

    def __init__(self):
        self.name = "cat"


ani = Animals('a', 'b')
cat = Cat()
# 集成了父类的限制
cat.a = "cat a"
cat.d = "d"
