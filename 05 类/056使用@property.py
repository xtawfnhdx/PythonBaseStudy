def D1():
    class Human(object):
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name

    hu = Human('张三')

    print(hu.name)
    # 这是一个属性，所以不能用 类.方法(参数) 的方式赋值，会报错"'str' object is not callable"
    hu.name = '李四'
    print(hu.name)


def D2():
    class Test2(object):
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

    t2 = Test2("张三")
    print(t2.name)
    # 只读属性，强制赋值，会报错“can't set attribute”
    # t2.name = '李四'


if __name__ == "__main__":
    D1()
    print('===============================')
    D2()
    print('===============================')
