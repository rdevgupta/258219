# Here in this example i learned how to pass one function as an argument to other functions

def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10
print(do_twice(add, a, b))