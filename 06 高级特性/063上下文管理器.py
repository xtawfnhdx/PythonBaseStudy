def D1():
    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def __enter__(self):
            pass


if __name__ == "__main__":
    print('D1================================')
    D1()
