import os

file = '076Test1.png'


def osAction():
    print('当前工作目录：', os.getcwd())
    print('绝对路径', os.path.abspath(file))
    print('相对路径', os.path.dirname(file))

    paths077 = os.path.join(os.getcwd(), '077')
    # 绝对路径删除
    if os.path.exists(paths077):
        os.rmdir(paths077)

    # 相对路径删除
    if os.path.exists('./077'):
        os.rmdir('./077')

    # 一次只能创建一层文件夹(相对路径创建)
    os.mkdir('./077')
    os.mkdir('./078-1')
    os.rename('./078-1', './078')


if __name__ == '__main__':
    osAction()
