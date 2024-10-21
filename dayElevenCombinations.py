from itertools import combinations
from itertools import permutations

s = [1, 2, 3]

print(list(permutations(s,2))) #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

print(list(combinations(s,2))) #[(1, 2), (1, 3), (2, 3)]

############# HAckerrank

# You are given a string S.
# Your task is to print all possible combinations, up to size k , of the string in lexicographic sorted order.

inputs = input().split()

S = sorted(str(inputs[0]))

k = int(inputs[1])

for i in range(k):
    lists = sorted(list(combinations(S,i+1)))

    for p in lists:
        print(''.join(p))
