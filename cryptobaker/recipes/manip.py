import re

class join:
    def __init__(self, delim=""):
        self.d = delim
    def cook(*args):
        d = getattr(args[0], "d", "")
        return d.join(args[-1])
    def __name__(*args):
        if args:
            return "join(%r)" % args[0].d
        return "join"

class split:
    def __init__(self, delim=" "):
        self.d = delim
    def cook(*args):
        d = getattr(args[0], "d", " ")
        return args[-1].split(d)
    def __name__(*args):
        if args:
            return "split(%r)" % args[0].d
        return "split"

class encode:
    def __init__(self, f="utf-8"):
        self.f = f
    def cook(*args):
        f = getattr(args[0], "f", "utf-8")
        return args[-1].encode(f)
    def __name__(*args):
        if args: return "encode(%r)" % args[0].f
        return "encode"

class decode:
    def __init__(self, f="utf-8"):
        self.f = f
    def cook(*args):
        f = getattr(args[0], "f", "utf-8")
        return args[-1].decode(f)
    def __name__(*args):
        if args: return "decode(%r)" % args[0].f
        return "decode"

class foreach:
    def __init__(self, fn):
        self.fn = fn
    def cook(self, raw):
        return [self.fn(i) for i in raw]
    def __name__(self):
        return "foreach(...)"

class splitevery:
    def __init__(self, i):
        self.i = i
    def cook(self, raw):
        return re.findall(("." * self.i) + "?", raw)
    def __name__(self):
        return "splitevery(%r)" % self.i

class regex:
    def __init__(self, exp):
        self.exp = exp
    def cook(self, raw):
        return re.findall(self.exp, raw)
    def __name__(self):
        return "regex(%r)" % self.exp