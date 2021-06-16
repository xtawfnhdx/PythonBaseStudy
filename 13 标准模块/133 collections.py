from collections import Counter, OrderedDict

s = 'ghgrhgredgfsdagfdsaaghrehtrehgfdhgbfdhewrthghdfshgdeshtr'
c = Counter(s)
print(c)
print(type(c))
# 其实就是一个字典对象
print(isinstance(c, dict))
# 取出次数最多的几个元素
print(c.most_common(3))

dictTest = dict([('a', 10), ('b', 20), ('c', 15)])

print(OrderedDict(dictTest))
