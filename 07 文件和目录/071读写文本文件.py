fileName = '074TestFile.txt'


def D1():
    with open(fileName, 'r') as file:
        str = file.read()
        print(str)


def D2():
    with open(fileName, 'r') as file:
        str = file.readlines()
        print(str)


def D3():
    with open(fileName, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line)


def D4():
    with open(fileName, 'r') as file:
        while True:
            line = file.read(20)
            if not line:
                break
            print(line)


# 结合yield 来使用
def D5():
    def read_in_chunks(file_Object, chunk_size=20):
        while True:
            strss = file_Object.read(chunk_size)
            if not strss:
                break
            yield strss

    with open(fileName, 'r') as file:
        for strings in read_in_chunks(file):
            print(strings)


# 文件对象是可迭代的
def D6():
    with open(fileName, 'r') as file:
        for i in file:
            print(i)
    with open(fileName, 'r') as file2:
        lins = list(file2)
        print(lins)


fileWriteName = "075TestFile.txt"


def D7():
    # 写入模式 文件存在：覆盖，文件不存在：创建 路径不存在：报错
    with open(fileWriteName, 'w') as file:
        file.write('write text string \n')
        file.write('write second string\n')

    with open(fileWriteName, 'a') as file2:
        file2.write('write three string')


if __name__ == "__main__":
    print('D1-----------------------')
    D1()
    print('D2-----------------------')
    D2()
    print('D3-----------------------')
    D3()
    print('D4-----------------------')
    D4()
    print('D5-----------------------')
    D5()
    print('D6-----------------------')
    D6()
    print('D7-----------------------')
    D7()
