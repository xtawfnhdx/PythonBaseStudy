# python 3 默认utf-8编码
import sys

print(sys.getdefaultencoding())

s='中文'
print(s.encode('utf-8'))

n='你好'
u=u'世界'
print(n+u)

# input 输入的类型是str
name=input('input you name:')
print(type(name))