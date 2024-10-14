# Sample Input

#  16 - Number of elements in set A
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52 - Elements of set A
#  4 - number of other sets

# - The first line of each part contains the space separated entries of the operation name and the length of the other set.
# - The second line of each part contains space separated list of elements in the other set.

#  intersection_update 10 
#  2 3 5 6 8 9 1 4 7 11 

#  update 2
#  55 66

#  symmetric_difference_update 5
#  22 7 35 62 58

#  difference_update 7
#  11 22 35 55 58 62 66

# Output Format

# Output the sum of elements in set A after apply all the mentioned operations

def setOperations(operation,aa,nn):
    if operation == 'intersection_update':
        aa.intersection_update(nn)
    elif operation == 'update':
        aa.update(nn)
    elif operation == 'difference_update':
        aa.difference_update(nn)
    elif operation == 'symmetric_difference_update':
        aa.symmetric_difference_update(nn)

    return aa

import sys

# read the number of elements in set A
a = int(input())
total = 0
# read the elements of set A
setA = set(map(int,input().split()))

#number of other sets
N = int(input())

for i in range(N):

    # read the set operation and the length of the set
    mutation, length = input().split()
    length = int(length)

    # read the elements of the set
    setN = set(map(int,input().split()))

    setA = setOperations(mutation,setA,setN)

for element in setA:
    total =+ element+total
# print(setA)
print(total)
    # print(operation,length)
    # print(setN)

    
