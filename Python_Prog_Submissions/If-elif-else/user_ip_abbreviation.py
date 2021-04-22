'''Write a python program to check the user input abbreviation.
If the user enters "lol", print "laughing out loud".
If the user enters "rofl", print "rolling on the floor laughing".
If the user enters "lmk", print "let me know".
If the user enters "smh", print "shaking my head".
'''

#code is menu driven select the options

print('''Enter your choice please: 
1. lol
2. rofl
3. lmk
4. smh
5. Exit from the Code
''')
choice = ""
while choice != "5":
    choice = input()
    if choice == "1":
        print("laughing out loud")
    elif choice == "2":
        print("rolling on the floor laughing")
    elif choice == "3":
        print("let me know")
    elif choice == "4":
        print("shaking my head")
    elif choice == "5":
        exit()
    else:
        print("Invalid choice! Try Again....") 
    print("Enter another choice: ") 
