# CryptoBaker

# Examples

## Good hashing recipe
```
from cryptobaker import *

hashr = lambda x: ("salt" + Dish(x).apply(toSHA256)).apply(toMD5)
print(hashr("password")) # '9f3b7f774efa78c8dd6df5e0ff1cb67d'
```

## Encoder and Decoder
```
from cryptobaker import *

encr = Recipe(toDecimal, toBinary, join(" "), toBase64)
decr = Recipe(fromBase64, split(" "), fromBinary, fromDecimal, join)

enc = encr.cook("Hello, world!")
dec = decr.cook(enc)

dec == "Hello, world!"
```