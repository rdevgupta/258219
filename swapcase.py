''' this is my code according to my inputs
string = input()
result = ""
for i in string:
    if i.isupper() == True:
        result += i.lower()
    elif i.islower() == True:
        result += i.upper()
    else:
        result += i
print(result) 


but i have changed it for hackerrank problem format like below: 
'''
def swap_case(s):
    result = ""
    for i in s:
        if i.isupper() == True:
            result += i.lower()
        elif i.islower() == True:
            result += i.upper()
        else:
            result += i
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)