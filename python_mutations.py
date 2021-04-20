#question is about how we can change or update a string as they are immutable means they can  not be changed
# there are two ways by slicing the string and join back
# second is convert the string into list as lists are mutable

'''
this is the second method of list

string = input()
print("before change string: "+string)
l = list(string)
character = 'K'
position = 3
l[position] = character
string = ''.join(l)
print(string)
'''

string = input()
print("before change string: "+string)
character = 'K'
position = 3
string = string[:3]+character+string[3:]
print("after change: "+string)
