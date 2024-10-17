#  A strict superset in set theory refers to a set that contains all the elements of another set, and has at least one additional element that the other set does not have.
#### This is a sample code to check strict super set            

# # Define two sets
A = {1, 2, 3}
B = {1, 2}

# Check if B is a strict superset of A
is_strict_superset = A > B  # This will return if A is strict super set of B

print(is_strict_superset)  # Output: True

#################################################################

#  Hackerrank
total = 0
# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
# Print True, if is A a strict superset of each of the sets. Otherwise, print False. 

#  The first line contains the space separated elements of set A. 
setA = set(map(int,input().split()))

# The second line contains integer , the n number of other sets. 
n = int(input())

#  The next n lines contains the space separated elements of the other sets. 
for i in range(n):
    setN = set(map(int,input().split()))
    is_str_superset = setA > setN  # This will return if setA is strict super set of setN

    if not is_str_superset:
        total =+ 1
if total>0:
    print (False)
else:
    print(True)
