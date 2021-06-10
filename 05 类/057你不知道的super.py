def D1():
    class Animal(object):
        def __init__(self, name):
            self._name = name

        def getName(self):
            print('this is a parent fun ')
            return self._name

    class Dog(Animal):
        def __init__(self, name):
            self._name = name

        def getName(self):
            return self._name

        # 仅仅是调用父类的方法，数据还是子类的，而不是父类的
        def getParentName(self):
            return super(Dog, self).getName()

    a = Animal('动物')
    d = Dog("小狗")
    print(a.getName())
    print(d.getName())
    print(d.getParentName())


def D2():
    class Basexx():
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def pr(self):
            print('this Base pr')

    class CA1(Basexx):
        def __init__(self, a, b, c):
            super().__init__(a, b)
            self._c = c

        def getAtrribute(self):
            print('a:', self.a)
            print('b:', self.b)
            print('c:', self._c)

    ca = CA1('gre', 'ger', 'nfr')
    ca.getAtrribute()
    ca.pr()


# super 无参数情况
def D3():
    class Base:
        def __init__(self):
            print('Base.init')

    class A(Base):
        def __init__(self):
            super().__init__()
            print('A.init')

    class B(Base):
        def __init__(self):
            super().__init__()
            print('B.init')

    class C(Base):
        def __init__(self):
            super().__init__()
            print('C.init')

    class D(A, B, C):
        def __init__(self):
            super().__init__()
            print('D.init')

    D()
    print(D.mro())


# super 传递一个参数
def D4():
    class Base:
        def __init__(self):
            print('Base.init')

    class A(Base):
        def __init__(self):
            super().__init__()
            print('A.init')

    class B(Base):
        def __init__(self):
            super().__init__()
            print('B.init')

    class C(Base):
        def __init__(self):
            super().__init__()
            print('C.init')

    class D(A, B, C):
        def __init__(self):
            # super() 只传递一个参数时，是一个不绑定的对象，不绑定的话它的方法是不会有用的
            super(B).__init__()
            print('D.init')

    D()
    print(D.mro())


def D5():
    class Base:
        def __init__(self):
            print('Base.__init__')

    class A(Base):
        def __init__(self):
            super().__init__()
            print('A.__init__')

    class B(Base):
        def __init__(self):
            super().__init__()
            print('B.__init__')

    class C(Base):
        def __init__(self):
            super().__init__()
            print('C.__init__')

    class D(A, B, C):
        def __init__(self):
            super(B, self).__init__()  # self是B的子类D的实例
            print('D.__init__')
            print(type(super(B, D).__init__))
            print(type(super(B, self).__init__))

    D()

    print(D.mro())


if __name__ == "__main__":
    print("D1==============================")
    # D1()
    print("D2==============================")
    D2()
    print("D3==============================")
    D3()
    print("D4==============================")
    D4()
    print("D5==============================")
    D5()
    print("D6==============================")
