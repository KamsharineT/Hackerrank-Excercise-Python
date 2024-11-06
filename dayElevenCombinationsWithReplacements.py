
from itertools import combinations_with_replacement
from itertools import combinations

c = [1, 2, 3]

print(list(combinations_with_replacement(c,2))) #[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
                                                

print(list(combinations(c,2))) #[(1, 2), (1, 3), (2, 3)]

#### Hackerrank

# You are given a string S.
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

read = input().split()

S = sorted(str(read[0]))

k = int(read[1])

# for i in range(k):
combs = list(combinations_with_replacement(S,k))

for c in combs:
    print(''.join(c))