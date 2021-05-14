class Animals(object):
    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex

    def getmes(self):
        print(self.name, self.__sex)


if __name__ == "__main__":
    ani = Animals("张三", "男")
    print(ani.name)
    ani.getmes()
    print('type:', type(ani))

    # 判断ani是否是指定类型的实例
    print(isinstance(ani, Animals))

    # 使用dir获取相应对象的所有属性和方法名称
    print(dir(ani))
