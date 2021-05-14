class Animals(object):
    bar = 1

    # 可以作为类的初始化补充函数
    # 如果有子类继承该类，调用静态方法，是调用的父类的，调用类方法，则是调用子类的
    @classmethod
    def animsg(cls):
        print('hello', cls)
        print(cls.bar)

    @staticmethod
    def static_fun():
        print('static fum')


Animals.animsg()
Animals.static_fun()
