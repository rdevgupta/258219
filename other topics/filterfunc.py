#removes items from list tha doesn't match
#the condition
nums = [11, 22, 33, 44, 55]
print("original list")
print(nums)
res = list(filter(lambda x: x%2 == 0, nums))
print("after filter list")
print(res)