#Write a Python program to convert a list of tuples into a dictionary

List = [("SFID", 258219), ("SFID", 258220), ("SFID", 258221), ("SFID", 258222), ("NAME", 'DEV'), ("NAME", 'SAGAR')]
Dict = {}
#create a dict with sfid and name seperately
for a, b in List:
    Dict.setdefault(a, []).append(b)
print (Dict)