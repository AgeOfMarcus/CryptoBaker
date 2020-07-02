import base64, urllib.parse, hexdump, uuid, html
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
_braille = {' ': '⠀', '!': '⠮', '"': '⠐', '#': '⠼', '$': '⠫', '%': '⠩', '&': '⠯', '': '⠄', '(': '⠷', ')': '⠾', '*': '⠡', '+': '⠬', ',': '⠠', '-': '⠤', '.': '⠨', '/': '⠌', '0': '⠴', '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢', '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔', ':': '⠱', ';': '⠰', '<': '⠣', '=': '⠿', '>': '⠜', '?': '⠹', '@': '⠈', 'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', '[': '⠪', '\\': '⠳', ']': '⠻', '^': '⠘', '_': '⠸'}

class toBase64:
    def cook(raw):
        return base64.b64encode(check(raw)).decode()
class fromBase64:
    def cook(raw):
        return dec(base64.b64decode(check(raw)))

class toAscii85:
    def cook(raw):
        return base64.a85encode(check(raw)).decode()
class fromAscii85:
    def cook(raw):
        return dec(base64.a85decode(check(raw)))

class toBase16:
    def cook(raw):
        return base64.b16encode(check(raw)).decode()
class fromBase16:
    def cook(raw):
        return dec(base64.b16decode(check(raw)))

class toBase32:
    def cook(raw):
        return base64.b32encode(check(raw)).decode()
class fromBase32:
    def cook(raw):
        return dec(base64.b32decode(check(raw)))

class toBase85:
    def cook(raw):
        return base64.b85encode(check(raw)).decode()
class fromBase85:
    def cook(raw):
        return dec(base64.b85decode(check(raw)))

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

class toURL:
    def cook(raw):
        return urllib.parse.quote_plus(raw)

class fromURL:
    def cook(raw):
        return urllib.parse.unquote(raw)

class toHexdump:
    def cook(raw):
        return hexdump.hexdump(check(raw), result="return")
    
class fromHexdump:
    def cook(raw):
        return hexdump.restore(raw)

class toUUID:
    def cook(raw):
        return str(uuid.UUID(bytes=check(raw)))
class fromUUID:
    def cook(raw):
        return dec(uuid.UUID(raw).bytes)

class toOctal:
    def cook(raw):
        return [oct(i)[2:] for i in raw]
class fromOctal:
    def cook(raw):
        return [int(i, 8) for i in raw]

class toHTML:
    def cook(raw):
        return html.escape(raw)
class fromHTML:
    def cook(raw):
        return html.unescape(raw)

class toBraille:
    def cook(raw):
        return ''.join([_braille.get(i.lower(), "?") for i in raw])
class fromBraille:
    def cook(raw):
        return ''.join([{v:k for k,v in _braille.items()}.get(i, "?") for i in raw])