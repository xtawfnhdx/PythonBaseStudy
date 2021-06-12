def D1():
    from math import sqrt, pow
    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Exit context")

        def __enter__(self):
            print('Enter context')
            return self

        def get_distance(self):
            distance = sqrt(pow(self.x, 2) + pow(self.y, 2))
            return distance

    with Point(3, 4) as pt:
        print('distance:', pt.get_distance())


def D2():
    from math import sqrt, pow
    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Exit context")
            return True

        def __enter__(self):
            print('Enter context')
            return self

        def get_distance(self):
            distance = sqrt(pow(self.x, 2) + pow(self.y, 2))
            return distance

    with Point(3, 4) as pt:
        print('distance:', pt.get_distance())
        # __exit__函数内部，返回True,即使报错，也不再抛出异常
        print('this is Error Fun', pt.thisError())


def D3():
    file = open('061迭代器.py', 'r')
    try:
        for line in file:
            print(line)
    finally:
        file.close()

    # 使用with 逻辑与上面同理
    with open('061迭代器.py', 'r') as file:
        for line in file:
            print(line)


# contextlib提供了上下文装饰器，但是内部获取资源与释放资源的代码，还需要自己实现
# yield 之前：获取资源代码   之后：释放资源代码
def D4():
    from contextlib import contextmanager

    @contextmanager
    def Point(fineName):
        str = "";
        fine = open(fineName, 'r')
        for line in fine:
            str += line

        yield str
        fine.close()

    with Point('061迭代器.py') as po:
        print(po)


if __name__ == "__main__":
    # print('D1================================')
    # D1()
    # print('D2================================')
    # D2()
    # print('D3================================')
    # D3()
    print('D4================================')
    D4()
