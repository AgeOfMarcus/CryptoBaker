class join:
    def __init__(self, delim=""):
        self.d = delim
        self.__name__ == 'join(%r)' % delim
    def cook(*args):
        d = getattr(args[0], "d", "")
        return d.join(args[-1])

class split:
    def __init__(self, delim=" "):
        self.d = delim
        self.__name__ = 'split(%r)' % delim
    def cook(*args):
        d = getattr(args[0], "d", " ")
        return args[-1].split(d)