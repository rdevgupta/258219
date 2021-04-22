#used to perform a certain operation on 
#iterables it takes func and iterable as
#an argument and perform func on each entry
# of iterable
def add_five(x):
    return x + 5

nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = list(map(add_five, nums))
print("list before func")
print(nums)
print("list after func")
print(result)