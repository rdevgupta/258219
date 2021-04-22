#sets are same as lists but unordered
#means can not be indexed
#dont contain duplicates
#add used to add
#remove to remove element
#pop remves arbitrary element
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

#union operation
print(first | second)
#intersection
print(first & second)
#difference
print(first - second)
print(second - first)
#symmetric difference element out of common
print(first ^ second)