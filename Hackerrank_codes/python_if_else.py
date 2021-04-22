'''if else if else statement explained in this code
hackerrank problem #2
'''
print("Enter the number please...")
number = int(input())
if number % 2 == 1:
    print("Weird")
elif number % 2 == 0 and 2 <= number <= 5:
    print("Not Weird")
elif number % 2 == 0 and 6 <= number <= 20:
    print("Weird")
else:
    print("Not Weird")