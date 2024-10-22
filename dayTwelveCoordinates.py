# You are given three integers and representing the dimensions of a cuboid

# let's say you are given three integers x, y, and z, which represent the dimensions of a cuboid (a 3D box). You are tasked with generating all possible coordinates (i, j, k) on this cuboid, where:

# i ranges from 0 to x
# j ranges from 0 to y
# k ranges from 0 to z

from itertools import combinations,permutations

x = int(input())
y = int(input())
z = int(input())
n = int(input())


lis = []

# List comprehension to generate the coordinates
coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

# Output the list of valid coordinates
# print(coordinates)

for c in coordinates:
    if sum(c) != n:
        lis.append(c)

print(lis)
