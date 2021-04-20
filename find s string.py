#question is about count the number of times substring is there in string
#dont confuse with count() method as it will tell you occurence of complete word but 
#half of one substring and half of other can generate desirede output as shown in coded testcases on hackerrank
string = input()
substr = input()
count = 0
for i in range(len(string) - len(substr) + 1):
    if (string[i:i+len(substr)] == substr):
            count += 1
print(count)

