# 列表是可变的
def begin():
    s = "hello"
    list_test = list(s)
    print('list_test type is:', type(list_test))
    tuple_test = (3, 4, 5, 6)
    list_test2 = list(tuple_test)
    print('list_test2 type is:', type(list_test2))
    print(list_test2)


# index 从列表中找出元素位置
def index_def():
    list_test1 = "this is a test string"
    print(list_test1.index("is"))
    print(list_test1.rindex("is"))
    # 找不到会报错
    # list_test1.index("ab")


# count 统计某个元素在列表中出现的次数
def count_def():
    list_test1 = "this is a test string"
    print(list_test1.count("is"))
    print(list_test1.count("ab"))
    # 必须要有一个参数
    # print(list_test1.count())


# 列表后面增加新的元素
def append_def():
    list_test = [1, 2, 3]
    list_test.append(4)
    print(list_test)
    list_test.append([5, 6, 7])
    print(list_test)


# 新列表增加到原列表中
def extend_def():
    list_test = [1, 2, 3, 4]
    list_test.extend([5, 6, 7])
    print(list_test)


# 将某个元素添加到某个位置
def insert_def():
    list_test = [1, 2, 3, 4]
    list_test.insert(3, 3)
    print((list_test))


# 移除一个元素并且返回这个元素的值
def pop_def():
    list_test = [1, 2, 3, 4]
    print(list_test.pop(2))
    print(list_test)


# 删除列表第一个匹配项
def remove_def():
    list_test = [1, 2, 3, 4, 5, 3, 2, 4, 2, 4, 4, 3, 2, 12]
    list_test.remove(3)
    print(list_test)


# 列表元素控制反转
def reverse_def():
    list_test = [1, 2, 3, 4, 5]
    list_test.reverse()
    print(list_test)


# 列表排序 直接修改原列表，而不生成新列表
def sort_def():
    list_test = [4, 2, 6, 63, 4, 5, 7, 3, 23, 5, 67, 7, 6, 9]
    list_test.sort()
    print(list_test)

    # 不改变原列表
    list_test = [4, 2, 6, 63, 4, 5, 7, 3, 23, 5, 67, 7, 6, 9]
    list_test2 = sorted(list_test)
    print("原始:", list_test)
    print("排序:", list_test2)

    # 倒叙
    list_test2.sort(reverse=True)
    print("倒序:", list_test2)

    # 关键字排序
    list_test3 = ['ge', 'gawgw', 'gcgrews', 'ads', 'gfgwssqwrwqgew', 'grewtg']
    list_test3.sort(key=len)
    print('len:', list_test3)

    # 第二个字符排序
    list_test3.sort(key=lambda s: s[1])
    print('第二个字符排序:', list_test3)

    students = [
        ('john', 'B', 15),
        ('jane', 'A', 12),
        ('dave', 'B', 10),
        ('ethan', 'C', 20),
        ('peter', 'B', 20),
        ('mike', 'C', 16)
    ]
    news = sorted(students, key=lambda s: (s[1], -s[2]))
    print(news)


if __name__ == "__main__":
    begin()
    index_def()
    count_def()
    append_def()
    extend_def()
    insert_def()
    pop_def()
    remove_def()
    reverse_def()
    sort_def()
