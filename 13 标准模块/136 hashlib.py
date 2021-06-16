import hashlib

# 必须为字符串指定编码，不然会报错
m = hashlib.md5('this is a string'.encode())
print(m.digest())
print(m.hexdigest())


m1=hashlib.md5()
m1.update('this'.encode())
m1.update(' is '.encode())
m1.update('a string'.encode())
print((m.hexdigest()))


h1=hashlib.sha1()
h1.update('this'.encode())
h1.update(' is '.encode())
h1.update('a string'.encode())
print(h1.hexdigest())
