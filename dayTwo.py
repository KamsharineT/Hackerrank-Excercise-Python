#import re


# pattern is a string containing the regex pattern
#pattern = r".*\+"

#try:
#	re.compile(pattern)
    
#except re.error:
#	print("Non valid regex pattern")
#	exit()


########## Read input from STDIN ###

# import sys

# for line in sys.stdin:
# 	if 'q' == line.rstrip():
# 		break
# 	print(f'Input : {line}')

# print("Exit")

############## hackerrank regex solution
def regex():
    import re
    n = int(input())
    for i in range(0,n):  
        try:
            input_ = input()
            a = (re.compile(input_))
            print(bool(a))
        except re.error:
            print('False')


###### Print Rangoli

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c---- 


# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------

# # def print_rangoli(size):
#     # your code goes here

#     odd = 2*size-1

#     for i in range(1,odd+1):
#         # print("-"*(size+1),end='')
#         print(chr(ord('a') + size-1))
#         # print("-"*(size+1))

# if __name__ == '__main__':
#     # print_rangoli(3)
#     # print(len("--------e--------"))

def print_rangoli(size):
    if(size == 1):
        print('a')
        return
    rangoli = ""
    
    middle = linePattern(size,0,1)
    lenLine = len(middle)
    
    for x in range(size -1,0,-1):
        rangoli += f"{linePattern(size,x,x+1,lenLine)}\n"
    rangoli += f"{middle}\n"
    for x in range(1,size,1):
        rangoli += f"{linePattern(size,x,x+1,lenLine)}\n"
    print(rangoli)
   
def linePattern(size, centerIndex, startIndex, width = 0):
    pattern = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in range(startIndex, size):
        if(x == size - 1):
            pattern += f"{alphabet[x]}"
        else:        
            pattern += f"{alphabet[x]}-" 
            
    return f"{pattern[::-1]}-{alphabet[centerIndex]}-{pattern}".center(width,'-')  

if __name__ == '__main__':
    print_rangoli(3)
    # print(len("--------e--------"))

