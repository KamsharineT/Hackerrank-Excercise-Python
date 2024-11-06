# this is a testing scripts for numpy polynomial

# The functions polyadd, polysub, polymul, and polydiv also 
# handle proper addition, subtraction, multiplication, and division of polynomial coefficients, respectively.

import numpy as np

l = [-1,1,1,10] # (x-1)(x+1)(x+1)(x+10) : answer (1,11,9,-11,-10)

print(np.poly(l))
#############################################
r = [1,0,-1] #x2+0x-1 = x2-1 = (x-1)(x+1) : answer (-1,1)

print(np.roots(r))
#############################################
i = [1, 1, 1]

print(np.polyint(i))
#############################################
d = [1, 1, 1, 1] 

print(np.polyder(d))
#############################################
v = [1, -2, 0, 2] #x3-2x2+0x+2 = x3-2x2+2 => x=4 =>>> 64 -32 +2 = 34

print(np.polyval(v,4)) 


######## Hackerrank 
#You are given the coefficients of a polynomial P.
# Your task is to find the value of P at point x.

r = list((input().split()))
float_list = [float(i) for i in r]

x = int(input())

c = np.polyval(float_list,x)

print(c)