#fibonacci using recursion
def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
#4th fibonacci term
print(fib(4))

#to print the series
num = int(input())
for i in range(num):
  print(fib(i))