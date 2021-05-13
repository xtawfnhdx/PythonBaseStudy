import functools


# map(fun,array)  => array中的 item 依次执行 fun(item)
def map_fun():
    def square(x):
        return x * x

    def double(x):
        return 2 * x

    def triple(x):
        return 3 * x

    print(list(map(square, [1, 2, 3])))
    print(list(map(lambda x: x * x, [1, 2, 3, 4])))
    print(list(map(str, [1, 2, 3])))
    print(list(map(int, ['1', '2', '3', '4'])))

    funcs = [square, double, triple]
    print(list(map(lambda f: f(4), funcs)))


# reduce(function, sequence[, initial]) 即：function(function(item1, item2), item3)
def reduce_fun():
    def square(x, y):
        return x * y

    print(functools.reduce(square, [1, 2, 3, 4, 5, 6]))
    f = lambda a, b: a if (a > b) else b
    print(functools.reduce(f, [666, 3, 5, 6, 3, 67, 4532, 4, 64, ]))
    print(functools.reduce(lambda x, y: x * y, [1, 2, 3], 4))
    print(functools.reduce(lambda x, y: x * y, [4, 1, 2, 3]))


# filter(function, sequnce) 将 function 依次作用于 sequnce 的每个 item，即 function(item)，
# 将返回值为 True 的 item 组成一个 List/String/Tuple (取决于 sequnce 的类型，python3 统一返回迭代器) 返回
def filter_fun():
    def test(x):
        return x > 50

    t1 = filter(test, [45, 465, 34, 43, 234, 5, 7, 5, 453, 4, 53, 543, 5])
    print(type(list(t1)), list(t1))
    t2 = filter(test, (45, 465, 34, 43, 234, 5, 7, 5, 453, 4, 53, 543, 5))
    print(type(list(t2)), list(t2))


if __name__ == "__main__":
    map_fun()
    print('=================================')
    reduce_fun()
    print('=================================')
    filter_fun()
