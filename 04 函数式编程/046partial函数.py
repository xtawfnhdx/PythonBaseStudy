import functools


def mark(x, y):
    return x - y


def mark2(x, y, z):
    return x - y - z


if __name__ == "__main__":
    # partial的功能：固定住函数mark的某个参数为默认值，然后返回一个新的函数
    f = functools.partial(mark, y=10)
    print(f(15))
    # 如果不指定参数是哪个，则默认将第一个参数实例化
    f = functools.partial(mark, 10)
    print(f(15))

    f2 = functools.partial(mark2, 5, 5)
    print(f2(10))

    f3 = functools.partial(mark2, z=4)
    print(f3(10, 2))
