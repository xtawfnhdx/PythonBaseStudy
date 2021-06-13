import argparse

parser = argparse.ArgumentParser()
# add_argument定义如何解析命令行参数
parser.add_argument('integer', type=int, help='display an integer')
args = parser.parse_args()

print(args.integer * 3)

# 终端中执行：
# >>>python 131\ argparse.py 123
