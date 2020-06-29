import base64
from .util import check, dec

class toBase64:
    def cook(raw):
        return base64.b64encode(check(raw)).decode()

class fromBase64:
    def cook(raw):
        return dec(base64.b64decode(check(raw)))

class toDecimal:
    def cook(raw):
        return list(map(ord, raw))

class fromDecimal:
    def cook(raw):
        return ' '.join(list(map(chr, raw)))

class toBinary:
    def cook(raw):
        return [format(x, 'b') for x in raw]

class fromBinary:
    def cook(raw):
        return [int(x, 2) for x in raw]

class toHex:
    def cook(raw):
        if " " in raw:
            raw = map(int, raw.split(" "))
        if type(raw) == str:
            raw = map(ord, raw)
        return [hex(i) for i in raw]

class fromHex:
    def cook(raw):
        return [int(x, 16) for x in raw]