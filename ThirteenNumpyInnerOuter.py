import numpy as np

A = np.array(list(map(int,input().split())))
B = np.array(list(map(int,input().split())))

innerarray = np.inner(A,B)
outerarray = np.outer(A,B)

print(innerarray)
print(outerarray)
