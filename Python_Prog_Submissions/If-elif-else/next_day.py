'''
Write a Python program to get next day of a given date using if-elif-else
'''
#to check if year is leap or not
def check_leap(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    else:
        return False

#to check the month
def check_month(month, leap):
    if month in (1, 3, 5, 7, 8, 10, 12):
        days = 31
    elif month == 2:
        if leap:
            days = 29
        else:
            days = 28
    else:
        days = 30
    return days

#main code
print("Enter the date month and year: ")
date = int(input())
month = int(input())
year = int(input())

#cheak leap year
leap = check_leap(year)

#check month and get the days
days = check_month(month, leap)

if date < days:
    date += 1
else:
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

#print the output
print("New date is: " + str(date) + ":" + str(month) + ":" + str(year))
