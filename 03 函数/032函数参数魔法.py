# 函数默认参数应该使用不可变参数！！
#
def begin(L=[]):
    print(id(L))
    L.append('end')
    return L


def begin2(L=()):
    L.append('end')
    return L


def param1(n=[]):
    print(id(n))
    n = n + [5]
    print(id(n))
    print(n)


def param2(n=[]):
    print(id(n))
    n.append(5)
    print(id(n))
    print(n)


# 可变参数
def paramNum_fun(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum += i
    print('sum:', sum)
    return sum


# 关键字参数1
def paramKey_def1(x, y, z):
    return x + y + z


# 关键字参数2
def paramKey_def2(**num):
    print(type(num))
    sum = 0
    for i, v in num.items():
        sum += v
    return sum


# 参数组合使用
# 参数顺序  必选参数 默认参数 可变参数 关键字参数
def paramList_def(x, y, z=0, *args, **kwargs):
    print('x:', x)
    print('y:', y)
    print('z:', z)
    print('*args:', args)
    print('**kwargs:', kwargs)


if __name__ == "__main__":
    # 输出 ['end']
    print(begin())
    # 输出 ['end', 'end']
    print(begin())
    # 输出 ['end', 'end', 'end']
    print(begin())
    # begin2()
    print('==================')
    x = [1, 2, 3]
    print(id(x))
    param1(x)
    print(x)
    print('==================')
    y = [1, 2, 3]
    print(id(y))
    param1(y)
    print(y)
    print('==================')
    print(paramNum_fun(3, 4, 5, 6, 7, 8))
    a = (3, 4, 5, 6, 7, 8)
    print(paramNum_fun(*a))
    print('==================')
    key1 = {'x': 1, 'y': 2, 'z': 3}
    print(paramKey_def1(key1["x"], key1['y'], key1['z']))
    print(paramKey_def1(**key1))
    print(paramKey_def2(**key1))
    print('==================')
    paramList_def(1, 2, 3, 4, 5, 6)
    paramList_def(1, 2, 4, u=6, v=7)
    paramList_def(1, 2, 3, 4, 5, 6, 7, u=8, v=9)
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    paramList_def(*a)
    # paramList_def(1, 2, 3, (5, 6, 7), {'x': 8, 'y': 9})
