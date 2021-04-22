'''Write a python program to check if the input number is
-real number
-float number
-string
-complex number
-Zero (0)
'''
number = input()
if number.isalpha():
    print("It's a String.")
elif number == "0":
    print("It's a Zero.")
elif number.isnumeric():
    print("It's a Integer or real number.")
else:
    try:
        number = float(number)
        print("It's a float number.")
    except:
        try:
            number = complex(number)
            print("It's a complex number")
        except:
            print("Invalid choice.")

