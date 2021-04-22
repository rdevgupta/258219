#Write a Python program to change the position of every n-th value with the (n+1)th in a list

from itertools import zip_longest, chain, tee

def operation(List):
    List1, List2 = tee(iter(List), 2)
    return list(chain.from_iterable(zip_longest(List[1::2], List[::2])))
n = [0,1,2,3,4,5]
print(operation(n))