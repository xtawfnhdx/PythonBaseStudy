# 迭代
# 一种遍历过程

# 可迭代对象
# 可以被遍历的对象
# 含有 “__iter__()” 或者 "__getitem__()"方法的对象

# 可以使用 hasattr()函数来判断是否包含某个方法，从而判断是否是可迭代对象
def D1():
    print('()', hasattr((), '__iter__'))
    print('[]', hasattr([], '__iter__'))
    print('{}', hasattr({}, '__iter__'))
    print(123, hasattr(123, '__iter__'))
    print(123, hasattr(123, '__getitem__'))
    print('abc', hasattr('abc', '__iter__'))
    print('abc', hasattr('abc', '__getitem__'))


if __name__ == "__main__":
    D1()
