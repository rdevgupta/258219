#named functions
def poly(x):
    return x**2 + 5*x + 4
print(poly(20))

#using lambda
print((lambda x: x**2 + 5*x +4) (20))