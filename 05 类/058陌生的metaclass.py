def D1():
    class Foo(object):
        foo = True

    class Bar(object):
        bar = True

    def echo(cls):
        return cls

    def select(name):
        if name == "foo":
            return Foo
        if name == "bar":
            return Bar

    # 将类作为一个函数传递
    print(type(echo(Foo())))

    # 动态构造一个类
    cls = select("foo")
    print(type(cls()))


# type 不止可以返回对象类型，还可以被用来动态的创建类
def D2():
    class FOO(object):
        pass

    # 参数1：定义类名
    # 参数2：元组，表示所有的父类
    Foo2 = type("Foo2", (object,), {})
    print(type(Foo2()))


def D3():
    def greet(self):
        print('hello')
        print(self.foo)

    res = type('FOO', (object,), {'foo': 'this is foo', 'greet': greet})
    res().greet()


# 元类(metaclass)：用来创建类(对象)的可调用对象
#
#   元类的主要目的是为了控制类的创建行为
#
def D4():
    class PrefixMetaclass(type):
        def __new__(cls, name, bases, attrs):
            # 给所有属性增加“my_”前缀
            _attrs = (("my_" + name, value) for name, value in attrs.items())
            # 转换为dict方法
            _attrs = dict((name, value) for name, value in _attrs)
            # 增加一个echo方法
            _attrs["echo"] = lambda self, phrase: phrase
            return type.__new__(cls, name, bases, _attrs)

    class FOO(metaclass=PrefixMetaclass):
        name = "foo"

        def bar(self):
            print('bar')

    # 当我们定义 class Bar(Foo) 时，Python 会首先在当前类，即 Bar 中寻找 __metaclass__，
    # 如果没有找到，就会在父类 Foo 中寻找 __metaclass__，如果找不到，就继续在 Foo 的父类寻找，如此继续下去，
    # 如果在任何父类都找不到 __metaclass__，就会到模块层次中寻找，如果还是找不到，就会用 type 来创建这个类。
    # 也就是说，元类会隐式地继承到子类
    class Bar(FOO):
        prop = 'bar'

    b = Bar()
    b.my_bar()
    print(b.my_name)
    print(b.my_prop)


if __name__ == "__main__":
    print('D1 =======================================')
    D1()
    print('D2 =======================================')
    D2()
    print('D3 =======================================')
    D3()
    print('D4 =======================================')
    D4()
