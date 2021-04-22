#hackerrank leap year find code solution
def is_leap(year):
    leap = False
    if year%400==0 :
        leap = True;
    elif year%4 == 0 and year%100 != 0:
        leap = True;
    return leap
    return leap

print("Enter the year you wanna check: ")
year = int(input())
print(is_leap(year))