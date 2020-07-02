from .recipes import *
from . import recipies as _recipies
import json

def Bake(raw, recipe):
    return Dish(recipe.cook(raw), recipe=recipe)

class Recipe(object):
    def __init__(self, *args):
        self.recipe = list(args)
    
    def cook(self, dish):
        dish = getattr(dish, "raw", dish)
        for r in self.recipe:
            dish = r.cook(dish)
        return dish
    
    def __repr__(self):
        return "<Recipe: %s>" % (" -> ".join(self.toDict()['recipe']))
    
    def append(self, recipe):
        self.recipe.append(recipe)
    def copy(self):
        return Recipe(*self.recipe)
    
    def toDict(self):
        return {'recipe': list(map((lambda x: x.__name__ if type(x.__name__) == str else x.__name__()), self.recipe))}

class Dish(object):
    def __init__(self, raw, recipe=Recipe()):
        self.raw = raw
        self.recipe = recipe
    
    def apply(self, recipe, *args, **kwargs):
        r = self.recipe.copy()

        if args or kwargs:
            recipe = recipe(*args, **kwargs)

        if type(recipe) == Recipe:
            r += recipe.recipe
        else:
            r.append(recipe)
        return Dish(recipe.cook(self.raw), recipe=r)
    
    def __repr__(self):
        return repr(self.raw)
    def __str__(self):
        if type(self.raw) == str:
            return self.raw
        return str(self.raw)
    
    def __add__(self, x):
        return Dish(self.raw + x, recipe=self.recipe)
    def __radd__(self, x):
        return Dish(x + self.raw, recipe=self.recipe)
    def __eq__(self, x):
        return self.raw == getattr(x, "raw", x)
    def __len__(self):
        return len(self.raw)
    def __nonzero__(self):
        return bool(self.raw)
    
    def __getitem__(self, key):
        return Dish(self.raw[key], recipe=self.recipe)
    def __setitem__(self, key, value):
        self.raw[key] = value
    def __iter__(self):
        return iter(map(Dish, self.raw))