def begin():
    str_test = "hello"
    print(str_test[1])
    print(str_test[1:3])
    print(str_test + " world")
    print(str_test * 3)


# 查找最左端索引
def find_def():
    str_test = "hello"
    print(str_test.find('l'))
    print(str_test.find('l', 3))


# split的反向操作
def join_def():
    list_test = ['a', 'b', 'c']
    print('+'.join(list_test))


# 移除两端匹配数据
def strip_def():
    str_test = '  hello world  '
    print(str_test.strip())
    str_test2 = '%% abc ##'
    print(str_test2.strip('#% '))


# 替换字符
def replace_def():
    str_test = 'this is a test string,is very good'
    print(str_test.replace('is', 'IS'))


def translate_def():
    str_test = 'this is a test string,is very good'
    table = str.maketrans('aeiou', '12345')
    print('替换', str_test.translate(table))
    print('原始', str_test)

    # 匹配到第三个参数全部删除
    table = str.maketrans('aeiou', '12345', 'th')
    str_test.translate(table)
    print('替换', str_test.translate(table))


if __name__ == "__main__":
    begin()
    find_def()
    join_def()
    strip_def()
    replace_def()
    translate_def()
