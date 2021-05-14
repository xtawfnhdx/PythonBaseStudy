def D1():
    def hello():
        return "hello world"

    def makeitalic(fun):
        def getMake():
            return '<li>' + fun() + '</li>'

        return getMake

    # 装饰器 的本质就是一个高阶函数
    # 装饰器可以定义多个，离函数最近的最先被调用
    @makeitalic
    @makeitalic
    def ShowHtml():
        return "this is text"

    def make_param_def(func, x, y):
        def abc():
            return '<' + x + '>' + func() + '</' + y + '>'

        return abc

    abc = makeitalic(hello)
    print(abc.__name__)
    print(abc())
    print(ShowHtml())
    print((hello()))


def D2():
    def make_funparam(func):
        def run(*args, **kwargs):
            ret = func(*args, **kwargs)
            return '<i>' + ret + '</i>'

        return run

    @make_funparam
    def hello(name):
        return 'hello ' + name

    @make_funparam
    def hello2(name1, name2):
        return 'hello ' + name1 + ',' + name2

    print(hello('张三'))
    print(hello2('张三', '李四'))


def D3():
    def waice(x1, x2):
        def make_funparam(func):
            def run(*args, **kwargs):
                ret = func(*args, **kwargs)
                return '<i>' + ret + '</i>' + x1 + x2

            return run

        return make_funparam

    @waice('x', 'y')
    def hello(name):
        return 'hello ' + name

    @waice('x', 'y')
    def hello2(name1, name2):
        return 'hello ' + name1 + ',' + name2

    print(hello('张三'))
    print(hello2('张三', '李四'))


def D4():
    def make1(func):
        def test1(*args1):
            return '(' + func(*args1) + ' this is make1)'

        return test1

    def make2(func):
        def test2(*args2):
            return '(' + func(*args2) + ' this is make2)'

        return test2

    def make3(text):
        def make2(func):
            def test2(*args2):
                return '(' + func(*args2) + ' this is make2)' + text

            return test2

        return make2

    @make1
    @make2
    def hello1():
        return 'hello'

    @make1
    @make2
    def hello2(name, name2):
        return 'hello ' + name + ' ' + name2

    @make3('text')
    @make1
    @make2
    def hello3(name, name2):
        return 'hello ' + name + ' ' + name2

    print(hello1())
    print(hello2('张三', '李四'))
    print(hello3('张三', '李四'))


def D5():
    # 类装饰器
    class Bold(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            return '<br>' + self.func(*args, **kwargs) + '</br>'

    @Bold
    def hello(*args):
        text = ''
        for x in args:
            text += x
        return 'hello' + text

    print(hello())
    print(hello('张三'))


# 如果类装饰器有参数，则__init__接收参数，而__call__接收func
def D6():
    # 类装饰器,带参数
    class Bold(object):
        def __init__(self, tag):
            self.tag = tag

        def __call__(self, func):
            def wappend(*args, **kwargs):
                return '<br>' + func(*args, **kwargs) + '</br>' + self.tag

            return wappend

    @Bold('abc')
    def hello(*args):
        text = ''
        for x in args:
            text += x
        return 'hello' + text

    print(hello())
    print(hello('张三'))


if __name__ == "__main__":
    D1()
    print('==================================')
    D2()
    print('==================================')
    D3()
    print('==================================')
    D4()
    print('==================================')
    D5()
    print('==================================')
    D6()
