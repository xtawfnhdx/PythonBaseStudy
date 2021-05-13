def begin():
    set_test = {}
    set_test = set('this is a set')
    print(set_test)
    set_test = set([12, 13, 14])
    print(set_test)
    set_test = {1, 2, 3, 'a', 'b', 'c', ('aa', 'bb', 'cc')}
    print(set_test)
    for v in set_test:
        print(v)
    set_test.add('abc')
    print(set_test)
    set_test.remove('abc')
    print(set_test)

    # discard删除不存在的数据，不会报错
    set_test.discard('abc')
    print(set_test)

    s1 = {1, 2, 3, 4, 5, 6}
    s2 = {3, 6, 9, 10, 12}
    print(s1 & s2)
    print(s1 | s2)
    print(s1 - s2)


if __name__ == "__main__":
    begin()
