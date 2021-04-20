string = input()
print("normal string")
print(string)
splitstr = string.split(" ")  #this will split the string where it find space in string
print("after splitting result string:")
print(splitstr)
joinstr = "-".join(splitstr)   # this will join the splitted string splitstr joining by - symbol
print("after joining the splitted string:")
print(joinstr)

