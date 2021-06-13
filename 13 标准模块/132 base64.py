import base64

# 后面字符串bytes类型
strs = b'hello world'
base64_str = base64.b64encode(strs)
print(base64_str)
print(type(base64_str))
print(base64.b64decode(base64_str))
