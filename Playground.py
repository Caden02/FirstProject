import math

# Version Two of Playground.py

class Foo:

  def __init__(self, foo):
    self.foo = foo

  def __eq__(self, other):
    """Implements ==."""
    return self.foo == other.foo

  def __repr__(self):
    # if you eval the return value of this function,
    # you'll get another Foo instance that's == to self
    return "Foo(%r)" % self.foo


c = Foo(5)

a = (c.__repr__())


p = math.pi
print(p)

class myclass():
    class_var = 1
    data = []

    def __init__(self, i_var, i_var2):
        self.i_var = i_var
        self.i_var2 = i_var2


    def f2(self):
        self.data.append(self.i_var + self.i_var2 + self.class_var)
        return self.data



class lim():
    limit = 10

    def __init__(self):
        self.data = []

    def item(self, i):
        return self.data[i]

    def add(self, e):
        if len(self.data) >= self.limit:
            raise Exception("Too many Elements")
        self.data.append(e)

l = lim()

xin = myclass(3, 4)

print(xin.f2())

gar = myclass

gar.a = 10, 12

print(gar.a)

foo = myclass(2, 3)

bar = myclass(3 ,4)

print(foo.__dict__)

print(bar.__dict__)

print(bar.f2())

print(foo.class_var, foo.i_var, foo.i_var2)

print(bar.class_var, bar.i_var)

print(foo.class_var, bar.i_var)
