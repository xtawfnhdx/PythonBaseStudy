def D1():
    try:
        x = input('Enter X:')
        y = input('Enter y:')
        print(type(x))
        print('%s' % str(int(x) / int(y)))
    except ZeroDivisionError as e:
        print('Error:', e)
    print('hello world')


def D2():
    try:
        # raise ZeroDivisionError('zero error')
        raise TypeError('Type Error string ')
    except ZeroDivisionError as e:
        print('this Zero Error:', e)
    except TypeError as e:
        print('this Type Error:', e)


def D3():
    # 自定义异常类
    class SomeError(Exception):
        pass

    try:
        raise SomeError('this is SomeError')
    except Exception as e:
        print('get a Error', e)


if __name__ == '__main__':
    print('D1-------------------------')
    # D1()
    print('D2-------------------------')
    D2()
    print('D3-------------------------')
    D3()
