# CryptoBaker

Installation:

* via pypi: `pip install cryptobaker`
* via githup: `pip install git+https://github.com/AgeOfMarcus/cryptobaker`
* from source:
```
$ git clone https://github.com/AgeOfMarcus/cryptobaker
$ cd cryptobaker
$ python setup.py install
```

# `Dish` and `Recipe` objects

The `Dish` object is what you start with. Recipes can only be applied to dishes. You create a dish like so: `x = Dish("Hello, world!")`

A `Recipe` object will be seen less often, but it can be useful in some cases. Let's say you've made a dish like so, `x = Dish("hello world").apply(toDecimal).apply(toMorse)`, and want to create another dish with the same recipe. The recipe of any dish can be accessed through the `.recipe` attribute, eg: `x.recipe` which will return `<Recipe: toDecimal -> toMorse>`. To make another dish with the recipe from `x`, you would do: `y = Bake("goodbye world", x.recipe)`. 

## recipes

Some recipes have no arguments, they are applied like so: `x.apply(toBase64)`. Some recipes require argument(s) and/or keyword argument(s), they can be applied in two ways, either like `x.apply(XOR("0110"))`, or like this `x.apply(XOR, "0110")`. Both do the same thing. 

Similarly, keyword arguments can be applied in two ways. `x.apply(toMorse(dot="*"))` or `x.apply(toMorse, dot="*")`.

Not all recipes begin with `to` or `from`. Some examples of recipies that don't are:

* `XOR` - this is because to reverse the process, you just apply XOR again with the same key
* `split` - this is a string manipulation method, it can be 'reversed' with `join`
* `join` - this is a list manipulation method, it can be 'reversed' with `split`

Not all recipes that begin with `to` have a counterpart. For example, all of the hashing recipes (such as `toSHA256`). This is because hashes are irreversable by nature.

## Examples

### Good hashing recipe
```
from cryptobaker import *

hashr = lambda x: ("salt" + Dish(x).apply(toSHA256)).apply(toMD5)
print(hashr("password")) # '9f3b7f774efa78c8dd6df5e0ff1cb67d'
```

### Encoder and Decoder
```
from cryptobaker import *

encr = Recipe(toDecimal, toBinary, join(" "), toBase64)
decr = Recipe(fromBase64, split(" "), fromBinary, fromDecimal, join)

enc = encr.cook("Hello, world!")
dec = decr.cook(enc)

dec == "Hello, world!"
```