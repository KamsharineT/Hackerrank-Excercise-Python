# itertools.permutations(iterable[, r])

# This tool returns successive r length permutations of elements in an iterable.

# If r is not specified or is None, then defaults to the length of the iterable, and all possible full length permutations are generated.

# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.


# Example

from itertools import permutations

s = [1,2,3]

print(permutations(s)) # <itertools.permutations object at 0x10439d3f0>

print(list(permutations(s))) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

print(list(permutations(s,None))) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

############# Hackerrank


# You are given a string s
# Your task is to print all possible permutations of size of k the string in lexicographic sorted order.

inputs = input().split()

lists = list(inputs[0])
try:
    val = int(inputs[1])
except:
    val = None

# Your task is to print all possible permutations of size of k the string in lexicographic sorted order.
perms = sorted(list(permutations(lists,val)))

for p in perms:
    print(''.join(p))
