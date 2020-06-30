from .recipes import *

class Recipe(object):
    def __init__(self, *args):
        self.recipe = list(args)
    
    def cook(self, dish):
        dish = getattr(dish, "raw", dish)
        for r in self.recipe:
            dish = r.cook(dish)
        return dish
    
    def __repr__(self):
        return "<Recipe: %s>" % (" -> ".join(map(lambda x: x.__name__, self.recipe)))
    
    def append(self, recipe):
        self.recipe.append(recipe)
    def copy(self):
        return Recipe(*self.recipe)

class Dish(object):
    def __init__(self, raw, recipe=Recipe()):
        self.raw = raw
        self.recipe = recipe
    
    def apply(self, recipe, arg=None):
        r = self.recipe.copy()

        if arg:
            recipe = recipe(arg)

        r.append(recipe)
        return Dish(recipe.cook(self.raw), recipe=r)
    
    def __repr__(self):
        return repr(self.raw)
    
    def __add__(self, x):
        return Dish(self.raw + x, recipe=self.recipe)
    def __radd__(self, x):
        return Dish(x + self.raw, recipe=self.recipe)
    def __eq__(self, x):
        return self.raw == getattr(x, "raw", x)