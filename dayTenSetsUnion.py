# # l = set(["ABCD"]) ## print {'ABCD'}

# h = set("ABCD") ## prints {'C', 'B', 'A', 'D'}

# print(h)
# k = set("EFGH")
# m = h.union("EFGH")

# y = h.union(k)

# print(h)

# print(m)

# print(y)

# s = set("Hacker")
# print (s.union("Rank"))
# # set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# print (s.union(set(['R', 'a', 'n', 'k'])))
# # set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

##### hackerrank


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

unionset = seten.union(setfn)

print(len(unionset))