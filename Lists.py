'''Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''
def operations():
    if choice[0]=='insert':
        Result.insert(int(choice[1]),int(choice[2]))
    elif choice[0]=='print':
        print(Result)
    elif choice[0]=='append':
        Result.append(int(choice[1]))
    elif choice[0]=='remove':
        Result.remove(int(choice[1]))
    elif choice[0]=='sort':
        Result.sort()
    elif choice[0]=='reverse':
        Result.reverse()
    elif choice[0]=='pop':
        Result.pop()

#main code
Result=[]
N = int(input())
for i in range(N):
    choice=str(input())
    choice=choice.split(' ')
    operations()