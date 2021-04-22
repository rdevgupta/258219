#question is about understanding of string built in validators
# like if string is alphanumeric or aplhabetic or digits only or lower and uppercase
string = input()
#to check if alphanumeric
print(string.isalnum())
#to check if complete aplhabetic
print(string.isalpha())
#to check if contains number only
print(string.isdigit())
#to check if completetely lowercase
print(string.islower())
#to check if completely uppercase
print(string.isupper())

'''
on hackerrank problem have to check characterwise follow the below code

print(any(char.isalnum() for char in S))
print(any(char.isalpha() for char in S))
print(any(char.isdigit() for char in S))
print(any(char.islower() for char in S))
print(any(char.isupper() for char in S))
'''