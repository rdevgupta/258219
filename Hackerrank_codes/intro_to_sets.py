size = int(input())
array = list(map(int, input().split()))
SET = set(array)
SUM = sum(SET)
SIZE = len(SET)
average = SUM/SIZE
print("answer is: "+ str(average))