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