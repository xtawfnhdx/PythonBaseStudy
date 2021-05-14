class Animals(object):
    def __init__(self, name):
        self.name = name

    def get_msg(self):
        return self.name


# 继承
class Dog(Animals):
    def get_msg(self):
        return 'this is dog:' + self.name

    def run(self):
        return "runing ~~"

