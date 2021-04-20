#my first medium level question in python
string = input()
k = int(input())
nstrings = int(len(string) / k)  #no. of subsegments

for index in range(nstrings):
    # Subsegment string
    t = string[index * k : (index + 1) * k]
    
    # Subsequence string having distinct characters
    u = ""
    
    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
            u += c

    # Print final converted string
    print(u)