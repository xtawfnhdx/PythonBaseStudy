import re

checkstring = 'one12twothree34four'
# 用于匹配正好一个对象
pattern = re.compile(r'\d+')
m = pattern.match(checkstring)
print(m)

m = pattern.match(checkstring, 2, 10)
print(m)

m = pattern.match(checkstring, 3, 10)
s = pattern.search(checkstring)
f = pattern.findall(checkstring)
fi = pattern.finditer(checkstring)
print('match---------------------')
print(m)
# 获取整个匹配的子串
print(m.group())
# 获取匹配的子串在字符串的起始位置
print(m.start())
# 获取匹配的子串在字符串的结束位置
print(m.end())
# 获取上述两个数据
print(m.span())
print('search---------------------')
print(s)
print(s.group())
print(s.span())
print('findall---------------------')
print(f)
print('finditer---------------------')
for i in fi:
    print(i)
    print(i.span())
    print(i.group())
print('---------------------')
checkStr = 'Hello World Wide Web'
# I表示忽略大小写
patt = re.compile(r'([a-z]+) ([a-z]+)', re.I)
p = patt.match(checkStr)
print(p.group(0))
print(p.span(0))
print(p.group(1))
print(p.span(1))
print(p.group(2))
print(p.span(2))
print(p.groups())
