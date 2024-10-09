
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    # to split the words and make an  list
    # eg = ['chris' , 'alan']
    s = s.split(' ')

    # to iterate through the list
    for i in range(len(s)):

        # make first letter capital
        s[i] = s[i].capitalize() #['Chris', 'Alan']

    return ' '.join(s)
if __name__ == '__main__':
    print(solve("chris alan"))