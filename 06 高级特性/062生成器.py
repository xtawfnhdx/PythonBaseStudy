# yield 把函数变成一个生成器，可以__next__  send throw close等操作
def D1():
    def IterFun():
        try:
            print('hello 1')
            yield 1
            print('hello 2')
            yield 2
            print('hello 3')
        except StopIteration:
            pass

    test = IterFun()
    print(test.__next__())
    print(test.__next__())
    # print(test.__next__())


def D2():
    def IterFun():
        try:
            value = 0
            value = yield 0
            print('value is ', value)
            value = yield 2
            print('value is ', value)
            value = yield 3
            print('value is ', value)
        except ValueError:
            print('ERROR')
        finally:
            print('END')

    iterfun = IterFun()
    print(iterfun.__next__())
    print(iterfun.send(5))
    print(iterfun.throw(ValueError))
    print(iterfun.close())
    print(type(iterfun))


if __name__ == "__main__":
    print('D1============================')
    D1()
    print('D2============================')
    D2()
