#print the repeated element in tuple

#entered numbers are 1, 2, 3, 4, 5, 6, 7, 8 and 1 3 5 are the repeated element
Tuple = (1,3,5,7,2,4,3,5,8,6,5,3,1)  
for i in Tuple:
    if Tuple.count(i) > 1:
        print('REPEATED %d' %i)