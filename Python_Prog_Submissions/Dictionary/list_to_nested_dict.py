# Write a Python program to convert a list into a nested dictionary of keys

List = [1, 2, 3, 4, 5, 6]
Final_Dict = Temp_Dict = {}
for i in List:
    #creates empty dict for each list item
    Temp_Dict[i] = {}
    #make that dict a key to final dict
    Temp_Dict = Temp_Dict[i]
print(Final_Dict)