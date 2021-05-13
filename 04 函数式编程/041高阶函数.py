# 函数中包含接收另一个函数作为参数的函数，即为高阶函数
def func(g, arry):
    return [g(x) for x in arry]


def doubles(x):
    return 2 * x


def square(x):
    return x * x


def GetSecondName(k, v):
    print(("%s %s") % (k, v))


def GetDictName(g, array=()):
    for k, v in array.items():
        g(k, v)


if __name__ == '__main__':
    print(func(doubles, [1, 2, 3, 4, 5, 6]))
    print(func(square, [1, 2, 3, 4, 5, 6]))
    GetDictName(GetSecondName, {'name': '张三', 'sex': '女', 'age': 12})
