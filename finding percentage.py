#hackerrank code for finding percentage problem in python
n = int(input())
dictionary = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    dictionary[name] = scores
query_name = input()

result = list(dictionary[query_name])
answer = sum(result)/len(result)
print("%.2f" % answer)