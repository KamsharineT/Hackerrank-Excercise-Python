from itertools import combinations

cnt = 0
N = int(input())

S = input().split()

r = int(input())

combs = list(combinations(S,r))

# Find all indices where 'a' occurs
indices_of_a = [index for index, value in enumerate(S) if value == 'a']

for c in combs:
    if 'a' in c:
        cnt += 1

t = round(cnt/len(combs),4)
print(t)

