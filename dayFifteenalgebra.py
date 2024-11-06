import numpy as np

arr = ([[1,2],[2,1]])

print(np.linalg.det(arr))

print (np.linalg.det([[1 , 2], [2, 1]])) # ==>> 1*2 - 2*2 = -3

print (np.linalg.det([[2 , 3], [3, 4]])) # ==> 2*4 - 3*3 = -1

print (np.linalg.det([[6,9], [10,20]]))

### find the determinant Hackerrank
l = []
N = int(input())
for i in range(N):
    arr = (input().split())
    arr = [float(a) for a in arr]
    l.append(arr)

print(l)

print(round(np.linalg.det(l),2))
