# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.


# The first line contains an integer, n, the number of students who have subscribed to the English newspaper. 

en = int(input())

# The second line contains n space separated roll numbers of those students. 
seten = set(map(int,input().split()))

# The third line contains b, the number of students who have subscribed to the French newspaper. 
fn = int(input())

# The fourth line contains b space separated roll numbers of those students. 
setfn = set(map(int,input().split()))

# enrolled for only english
onlyen = seten.difference(setfn)

print(len(onlyen))