# 迭代
# 一种遍历过程

# 可迭代对象
# 可以被遍历的对象
# 含有 “__iter__()” 或者 "__getitem__()"方法的对象

# 可以使用 hasattr()函数来判断是否包含某个方法，从而判断是否是可迭代对象
def D1():
    print('()', hasattr((), '__iter__'))
    print('[]', hasattr([], '__iter__'))
    print('{}', hasattr({}, '__iter__'))
    print(123, hasattr(123, '__iter__'))
    print(123, hasattr(123, '__getitem__'))
    print('abc', hasattr('abc', '__iter__'))
    print('abc', hasattr('abc', '__getitem__'))

    print('(1,2,3):__iter__:', hasattr((1, 2, 3), '__iter__'))
    print('(1,2,3):__next__:', hasattr((1, 2, 3), '__next__'))


# 版本问题，导入的时候，需要增加.abc
from collections.abc import Iterable, Iterator


# 可迭代对象，未必是迭代器
def D2():
    # 验证是否可以被迭代
    print('()是否可以被迭代：', isinstance((), Iterable))
    # 验证是否是迭代器(与上面有区别)
    print('()是否是迭代器：', isinstance((), Iterator))

    # 验证是否可以被迭代
    print('[]是否可以被迭代：', isinstance([], Iterable))
    # 验证是否是迭代器(与上面有区别)
    print('[]是否是迭代器：', isinstance([], Iterator))

    # 验证是否可以被迭代
    print('{}是否可以被迭代：', isinstance({}, Iterable))
    # 验证是否是迭代器(与上面有区别)
    print('{}是否是迭代器：', isinstance({}, Iterator))


def D3():
    temp = "abcde"
    iter_temp = iter(temp)
    print('iter_temp:', isinstance(iter_temp, Iterable))
    # python3 里面获取下一个元素，是“__next__”
    print(iter_temp.__next__())
    print(iter_temp.__next__())


def D4():
    text = [1, 2, 3, 4, 5]
    # for循环，其实就是内部调用了iter，获取到迭代器对象，然后挨个输出下一个字符
    for x in text:
        print(x)
    iter_text = iter(text)

    # for循环等价于如下函数代码
    while True:
        try:
            print(iter_text.__next__())
        except StopIteration:
            break


# 练习：创建一个迭代器
def D5():
    class Fib(object):
        def __init__(self):
            self.a, self.b = 0, 1

        def __iter__(self):
            return self

        def __next__(self):
            self.a, self.b = self.b, self.a + self.b
            return self.a

    fib = Fib()
    for i in fib:
        if i > 10:
            break
        print(i)


if __name__ == "__main__":
    print("D1 ===============================================================")
    D1()
    print("D2 ===============================================================")
    D2()
    print("D3 ===============================================================")
    D3()
    print("D4 ===============================================================")
    D4()
    print("D5 ===============================================================")
    D5()
