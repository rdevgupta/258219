records=[]
scores=[]
output=[]
n=int(input())
for _ in range(n):
    name = input()
    score = float(input())
    records.append([name, score])
    scores.append(score)
    scores.sort()
for i in range(len(scores)):
    if scores[i]<scores[i+1]:
        x=scores[i+1]
        break
for i in range(n):
    if records[i][1]==x:
        output.append(records[i][0])
        output.sort()
for j in range(len(output)):
    print(output[j])