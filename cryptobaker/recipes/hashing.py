import hashlib
from .util import check

class toMD5:
    def cook(raw):
        return hashlib.md5(check(raw)).hexdigest()

class toSHA1:
    def cook(raw):
        return hashlib.sha1(check(raw)).hexdigest()

class toSHA224:
    def cook(raw):
        return hashlib.sha224(check(raw)).hexdigest()

class toSHA256:
    def cook(raw):
        return hashlib.sha256(check(raw)).hexdigest()

class toSHA384:
    def cook(raw):
        return hashlib.sha384(check(raw)).hexdigest()

class toSHA512:
    def cook(raw):
        return hashlib.sha512(check(raw)).hexdigest()