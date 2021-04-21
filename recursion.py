#func that calls itself till the base case hits
def factorial(x):
    #base case
    if x == 1:
        return 1
    else:
        #calling loop
        return x * factorial(x - 1)
#output of factorial 5 using recursion
print(factorial(5))