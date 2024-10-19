
# s = set([1,2,3,4,5,6,7,8,9])

# s.remove(5)

# print(s)
# print(s.remove(7))

# # discard returns None if value doesn't exist 
# s.discard(10)

# print(s)

# s.discard(6)

# print(s)

# # pop removes the first element
# s.pop()

# print(s)

# k = set([1])

# # if pop removes the only one existing element it gives an empty set
# k.pop()

# print(k)
# # remove returns key error if value doesn't exist 
# s.remove(10)


##### Hackerrank

# # The first line contains integer n, the number of elements in the set s .
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

def commands(sets,commandlist):

    # print('sets',sets)
    command = commandlist[0]
    try:
        val = int(commandlist[1])
    except:
        val = None
    if command == 'pop':
        sets.pop()
    elif command == 'remove':
        sets.remove(val)
    elif command == 'discard':
        sets.discard(val)


n = int(input())
s = set(map(int, input().split()))

ns = int(input())

for i in range(ns):

    # receive the command as a list (either pop, remove and/or discard commands followed by their associated value.)
    commandlist = input().split()
    commands(s,commandlist)

# print(s)

# to Print the sum of the elements of set s on a single line.
print(sum(s))