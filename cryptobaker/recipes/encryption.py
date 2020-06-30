from .errors import ArgumentException

class XOR:
    def __init__(self, dat):
        self.dat = dat
    def cook(*args):
        dat = getattr(args[0], "dat", False)
        if not dat: raise ArgumentException
        dat = getattr(dat, "raw", dat)
        raw = getattr(args[-1], "raw", args[-1])
        if type(raw) == list:
            res = []
            for i in range(0,len(raw)):
                res.append(bin(int(raw[i], 2) ^ int(dat[i], 2))[2:].zfill(len(raw[i])))
            return res
        else:
            try:
                return raw ^ dat
            except:
                return bin(int(raw, 2) ^ int(dat, 2))[2:].zfill(len(raw))
    def __name__(self):
        return "XOR(%r)" % self.dat