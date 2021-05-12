def begin():
    # 列表
    list_test = [1, 2, 3, 4, 5, 6, 7]
    # 字符串
    str_test = "this is test string"
    # 元组
    tuple_test = (34, 4, 5, 56, 6, 7, 89)
    print(list_test[2])
    print(str_test[2])
    print(tuple_test[2])

    print(list_test[-2])
    print(str_test[-2])
    print(tuple_test[-2])


# 分片
def slicing():
    str_test = "this is test string"
    print(str_test[2:8])
    print(str_test[-3:])
    print(str_test[:5])


# 步长
def step():
    str_test = "this_is_test_step"
    print(str_test[3:10:2])
    print(str_test[:-5:-1])


def add():
    str_test1 = "test1"
    str_test2 = "test2"
    print(str_test1 + str_test2)


def multiply():
    str_test1 = "zhangsan"
    print(str_test1 * 3)


def check_in():
    str_test = "this is a test"
    print('is ' in str_test)
    print('ab' in str_test)
    tuple_test = (3, 4, 5, 6, 7)
    print(4 in tuple_test)


if __name__ == "__main__":
    # begin()
    # slicing()
    # step()
    add()
    multiply()
    check_in()
