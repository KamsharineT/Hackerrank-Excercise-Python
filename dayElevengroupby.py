from itertools import groupby
from collections import Counter

# s = [1, 2, 3]

# print(list(groupby(s)))

# Python code to demonstrate 
# itertools.groupby() method 




L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)] 

# Key function 
key_func = lambda x: x[0] 

for key, group in groupby(L, key_func): 
	print(key + " :", list(group)) 
	
S = tuple(str(input()))

print(S)
# Key function 
key_func = lambda x: x[0] 

for key,group in groupby(S,key_func):

    # print("("+str(len(list(group)))+", "+str(key)+")",end=' ') 
    val = "("+str(len(list(group)))+", "+str(key)+")"
    print(val,end=" ")