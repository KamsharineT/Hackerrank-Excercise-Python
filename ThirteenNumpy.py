
import numpy as np

A = np.array([0,1])
B = np.array([3,4])

print(np.inner(A,B))

print(np.outer(A,B))

import numpy as np

# For 1D arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.inner(a, b)
print(result)  # Output: 32
# Explanation: 1*4 + 2*5 + 3*6 = 32

# For 2D arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.inner(A, B)
print(result)
# Output:
# [[17 23]
#  [39 53]]
# Explanation: Row-wise inner products:
# [1*5 + 2*6, 1*7 + 2*8] => [17, 23]
# [3*5 + 4*6, 3*7 + 4*8] => [39, 53]
