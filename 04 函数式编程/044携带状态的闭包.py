'''
闭包是携带自由变量的函数，即使创建闭包的外部函数的生命周期结束了，闭包所引用的自由变量仍会存在。
闭包在运行可以有多个实例。
尽量不要在闭包中引用循环变量，或者后续会发生变化的变量。
'''

from math import pow, sqrt


def mark_pow(n):
    def inner_pow(x):
        return pow(x, n)

    return inner_pow


def point(x, y):
    def get_distance(u, v):
        return sqrt((x - u) ** 2 + (y - v) ** 2)

    return get_distance


def count_test():
    func = []
    for i in [1, 2, 3]:
        def g(param):
            f = lambda: param + 3
            return f

        func.append(g(i))
    return func


if __name__ == '__main__':
    pownew = mark_pow(3)
    count = pownew(2)
    print(count)

    print('==============================')
    # del mark_pow
    # 报错
    # pownew2=mark_pow(3)
    # print(pownew(5))
    print('==============================')
    # 闭包可以运行多个实例
    pownew2 = mark_pow(3)
    print(pownew == pownew2)
    print('==============================')
    pointA = point(5, 5)
    print(pointA(9, 9))
    print(pointA(13, 13))
    print('==============================')
    f1, f2, f3 = count_test()
    print(f1())
    print(f2())
    print(f3())
