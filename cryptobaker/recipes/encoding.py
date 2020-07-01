import base64, urllib.parse, hexdump
from .util import check, dec

_morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', ' ': '/'
}

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
        return list(map(chr, raw))

class toBinary:
    def cook(raw):
        return [format(x, 'b') for x in raw]

class fromBinary:
    def cook(raw):
        if ' ' in raw:
            raw = raw.split(" ")
        return [int(x, 2) for x in raw]

class toHex:
    def cook(raw):
        if type(raw) == str:
            raw = map(ord, raw)
        return [hex(i) for i in raw]

class fromHex:
    def cook(raw):
        return [int(x, 16) for x in raw]

class toMorse:
    def __init__(self, dot=".", dash="-", unknown="?"):
        self.dot = dot
        self.dash = dash
        self.unknown = unknown
    def cook(*args):
        dot = getattr(args[0], "dot", ".")
        dash = getattr(args[0], "dash", "-")
        unknown = getattr(args[0], "unknown", "?")

        return ' '.join([_morse.get(i.upper(), unknown) for i in args[-1]]).replace(".", dot).replace("-", dash)
    def __name__(*args):
        if len(args) == 0:
            return "toMorse"
        else:
            self = args[0]
            return "toMorse(dot=%r, dash=%r, unknown=%r)" % (
                self.dot, self.dash, self.unknown
            )

class fromMorse:
    def __init__(self, dot=".", dash="-", unknown="?"):
        self.dot = dot
        self.dash = dash
        self.unknown = unknown
    def cook(*args):
        dot = getattr(args[0], "dot", ".")
        dash = getattr(args[0], "dash", "-")
        unknown = getattr(args[0], "unknown", "?")

        return ''.join([{y:x for x,y in _morse.items()}.get(i.upper(), unknown) for i in args[-1].replace(dot, ".").replace(dash, "-").split(" ")])
    def __name__(*args):
        if len(args) == 0:
            return "fromMorse"
        else:
            self = args[0]
            return "fromMorse(dot=%r, dash=%r, unknown=%r)" % (
                self.dot, self.dash, self.unknown
            )

class URLEncode:
    def cook(raw):
        return urllib.parse.quote_plus(raw)

class URLDecode:
    def cook(raw):
        return urllib.parse.unquote(raw)

class toHexdump:
    def cook(raw):
        return hexdump.hexdump(check(raw), result="return")
    
class fromHexdump:
    def cook(raw):
        return hexdump.restore(raw)