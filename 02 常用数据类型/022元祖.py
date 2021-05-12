# 元组是一种不可变序列
def begin():
    a = (1, 2, 3)
    print(a)
    print(())

    # 创建只包含一个数据的元组，后面一定要加个逗号！！
    b = (1,)
    print(type(b))

    # 不加逗号的，本质上代表一个字符串或者数字
    c = (10)
    print(type(c))


def index_def():
    tuple_test = (1, 2, 3, 4, 5, 6)
    print(tuple_test.index(3))


def slicing_def():
    tuple_test = (1, 2, 3, 4, 5, 6, 7)
    print(tuple_test[1:4])


if __name__ == "__main__":
    begin()
    index_def()
    slicing_def()
