def begin():
    dict_test = {}
    print(type(dict_test))
    dict_test = {'name': 'zhangsan', 'age': 22}
    print(dict_test["age"])
    dict_test2 = dict(name='lisi', sex='woman')
    print(dict_test2)
    dict_test3 = dict([('name', 'wangwu'), ('age', 'man')])
    print(dict_test3)


def foreach_def():
    dict_test = {'name': 'lisi', 'sex': 'woman'}
    for key in dict_test:
        print(key, dict_test[key])
    print(dict_test)


def in_def():
    dict_test = {'name': 'lisi', 'sex': 'woman'}
    print('sex' in dict_test)
    print('abc' in dict_test)


import copy


def commonly_used():
    dict_test = {'name': 'lisi', 'sex': 'woman'}
    print('clear:', dict_test.clear())

    '''
    ======================================
    copy 这个是浅复制
    ======================================'''

    dict_test = {'name': 'lisi', 'home': ['home1', 'home2', 'home3']}
    dict_test2 = dict_test.copy()
    print('copy:', dict_test2)

    # "lisi"属于字符串，属于不可变对象，随意即使是浅复制，对“dict_test”的修改也不会影响到“dict_test2”
    dict_test['name'] = 'wangwu'
    print('修改:', dict_test)
    print('修改:', dict_test2)

    # home的值是 list，属于可变对象，所以将“dict_test”的值修改以后，“dict_test2”的值也相对应一起变化
    dict_test = {'name': 'lisi', 'home': ['home1', 'home2', 'home3']}
    dict_test2 = dict_test.copy()
    dict_test['home'].remove('home2')
    print('修改2:', dict_test)
    print('修改2:', dict_test2)

    '''
    ======================================
    deepcopy 这个是深复制
    ======================================'''
    # home的值是 list，属于可变对象，即使“dict_test”的值修改以后，“dict_test2”的值也不会变化
    dict_test = {'name': 'lisi', 'home': ['home1', 'home2', 'home3']}
    dict_test2 = copy.deepcopy(dict_test)
    dict_test['home'].remove('home2')
    print('深复制-修改2:', dict_test)
    print('深复制-修改2:', dict_test2)

    '''
    ======================================
    get
    ======================================'''
    dict_test = {'name': 'lisi', 'home': ['home1', 'home2', 'home3']}
    print(dict_test.get("name"))
    print(dict_test.get("name2"))

    '''
    ======================================
    setdefault
    ======================================'''
    dict_test = {}
    dict_test.setdefault('name', '张三')
    print('setdefault:', dict_test)
    dict_test['sex'] = '女'
    print('setdefault:', dict_test)
    # 当存在默认值，重新设定默认值时，不覆盖原来默认值，并且返回原来默认值
    print(dict_test.setdefault('name', '李四'))
    print('setdefault:', dict_test)

    '''
    ======================================
    update 讲一个字典添加到原字典中，存在相同则覆盖
    ======================================'''
    dict_test = {}
    dict_test = {'name': '张三'}
    print('update:', dict_test)
    dict_test.update({'name': '李四'})
    print('update:', dict_test)

    '''
    ======================================
    items/iteritems
    ======================================'''
    dict_test = {'name': '张三', 'sex': '女', 'home': '武汉'}
    print('itmes:', dict_test.items())
    for k, v in dict_test.items():
        print(k, v)

    '''
    ======================================
    keys
    ======================================'''
    dict_test = {'name': '张三', 'sex': '女', 'home': '武汉'}
    print('values:', dict_test.keys())
    for k in dict_test.keys():
        print(k)

    '''
    ======================================
    values
    ======================================'''
    dict_test = {'name': '张三', 'sex': '女', 'home': '武汉'}
    print('values:', dict_test.values())
    for v in dict_test.values():
        print(v)

    '''
    ======================================
    pop/popitem   popitem 随机移除
    ======================================'''
    dict_test = {'name': '张三', 'sex': '女', 'home': '武汉'}
    print('pop:', dict_test.pop('sex'))
    print('popitem:', dict_test.popitem())
    print('pop:', dict_test)


if __name__ == "__main__":
    begin()
    foreach_def()
    in_def()
    commonly_used()
