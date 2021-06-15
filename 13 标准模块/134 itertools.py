import itertools

# count 生成一个无线循环序列的迭代器
# 第一个参数：循环初始值
# 第二个参数：步长
print('count-------------------------------')
nums = itertools.count()
for i in nums:
    if i > 10:
        break
    print(i)

nums = itertools.count(2, 3)
for i in nums:
    if i > 20:
        break
    print(i)

# cycle:生成一个有限迭代器
# 将参数执行迭代
print('cycle-------------------------------')
cirtest = itertools.cycle('abcd')
i = 1
for ct in cirtest:
    if i > 10:
        break
    print(ct)
    i += 1

# repeat反复生成object，如果给定times，则重复次数为times，否则为无限
print('repeat-------------------------------')
re = itertools.repeat('abcde', 5)
for r in re:
    print(r)

# chain将多个可迭代对象作为参数，合并起来返回一个新的迭代器对象
print('chain-------------------------------')
for item in itertools.chain([1, 2, 3], ['a', 'b']):
    print(item)

# compress 对数据进行筛选，当某个元素为true时，保留，否则去除
print('compress-------------------------------')
print(list(itertools.compress('abcdef', [1, 0, 0, 1, 1, 1])))

# dropwhile(predicate,iterable)
# predicate:函数，对于iterable中的元素，如果predicate(item)=true,则丢弃该元素
print('dropwhile-------------------------------')
print(list(itertools.dropwhile(lambda x: x < 5, [1, 3, 6, 4, 5, 3, ])))

# groupbyd对序列进行分组
print('dropwhile-------------------------------')
for key, value_iter in itertools.groupby('aaagbbbddddddeee'):
    print(key, list(value_iter))

print('dropwhile2-------------------------------')
for key, value_iter in itertools.groupby(['a', 'b', 'ccc', 'dd', 'f'], len):
    print(key, list(value_iter))

# ifilter:将 iterable 中 function(item) 为 True 的元素组成一个迭代器返回，
# 如果 function 是 None，则返回 iterable 中所有计算为 True 的项
print('ifilter-------------------------------')
# Python3中没有ifilter函数，和自带的filter函数功能一样
print(list(filter(lambda x: x < 6, range(10))))

# islice:切片选择
print('islice-------------------------------')
print(list(itertools.islice([1,2,3,4,54,6,7,8,9,4],5)))

