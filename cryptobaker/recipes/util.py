def check(raw):
    if type(raw) == str:
        return raw.encode()
    elif type(raw) == list or type(raw) == tuple:
        try:
            return bytes(list(raw))
        except TypeError:
            return ' '.join(list(raw)).encode()
    elif type(raw) == int:
        return bytes([raw])
    else:
        return raw

def dec(raw):
    try:
        return raw.decode()
    except:
        return raw