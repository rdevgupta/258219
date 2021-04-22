#Question:- Write a Python script to merge two Python dictionaries

#first dictionary
dictionary_first = {'SFID': "258219", 'NAME': "Dev Gupta", 'MODULE': "Python"}

#second dictionary
dictionary_second = {'TRACK': "STEPIN", 'BRANCH': "SOFTWARE", 'EMAIL': "guptadev359@gmail.com"}

#merge both to first and print it
print("Before merging first dictionary: ")
print(dictionary_first)
dictionary_first.update(dictionary_second)
print("After merging first dict. changed but second remains the same: ")
print(dictionary_first)
print(dictionary_second)