# The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both. 

# The first line contains an integer, n, the number of students who have subscribed to the English newspaper. 

en = int(input())

# The second line contains n space separated roll numbers of those students. 
seten = set(map(int,input().split()))

# The third line contains b, the number of students who have subscribed to the French newspaper. 
fn = int(input())

# The fourth line contains b space separated roll numbers of those students. 
setfn = set(map(int,input().split()))

notboth = seten.symmetric_difference(setfn)
print(notboth)
print(len(notboth))
