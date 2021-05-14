class Animial(object):
    _dict = dict()

    def __new__(cls, *args, **kwargs):
        if 'key' in Animial._dict:
            print('EXISTS')
            return Animial._dict["key"]
        else:
            print("new")
            return object.__new__(cls)
        return Animial()

    def __init__(self):
        print('init')
        Animial._dict['key'] = self


a = Animial()
b = Animial()
