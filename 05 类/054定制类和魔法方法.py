def D1():
    class Animial(object):
        _dict = dict()

        def __new__(cls, *args, **kwargs):
            if 'key' in Animial._dict:
                print('EXISTS')
                return Animial._dict["key"]
            else:
                print("new")
                return object.__new__(cls)
            return Animial()

        def __init__(self):
            print('init')
            Animial._dict['key'] = self

    a = Animial()
    b = Animial()


def D2():
    class Test01():
        def __str__(self):
            return 'this Is str'

        def __repr__(self):
            return 'this is repr'

        def __init__(self):
            self.name = "test01"

    t = Test01()
    print(t)
    print(str(t))
    print(str([t]))

    import datetime
    today = datetime.datetime.now()
    print(str(today))
    print(repr(today))


def D3():
    class Fib(object):
        def __init__(self):
            self.a, self.b = 0, 1

        def __iter__(self):
            return self

        def __next__(self):
            self.a, self.b = self.b, self.a + self.b
            return self.a, self.b

    fib = Fib()
    for i, j in fib:
        if i > 10:
            break
        print(i, j)


def D4():
    class Fib(object):
        def __getitem__(self, item):
            i, j = 0, 1
            for x in range(item):
                i, j = j, i + j
            return i

    fib = Fib()
    print(fib[4], fib[6], fib[12])
    print(fib)


def D5():
    class Fib(object):
        def __init__(self):
            self.a = 1
            self.b = 2

        def __getattr__(self, item):
            if item == "c":
                return 0
            return AttributeError('Point object has not attribute')

    fib = Fib()
    print(fib.a)
    print(fib.b)
    print(fib.c)
    print(fib.d)


def D6():
    class Point(object):
        def __init__(self):
            self.a = 1
            self.b = 2

        def __call__(self, args):
            return self.a + self.b + args

    po = Point()
    print(callable(po))
    print(po(5))


if __name__ == '__main__':
    D1()
    print('=============================')
    D2()
    print('=============================')
    D3()
    print('=============================')
    D4()
    print('=============================')
    D5()
    print('=============================')
    D6()
