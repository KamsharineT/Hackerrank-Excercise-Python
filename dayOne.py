## 2024-09-26
##################### end = '' ###################

n=10

def one(n):
    for i in range(n):
        print(i)

def two(n):
    for i in range(n):
        print(i+1,end='')

def three(n):
    for i in range(1,n+1):
        print(i,end='') 

def four():
    print('hello ')
    print('world!')

def five():
    print('hello ',end='')
    print('world!')
two(n) 
print('')
three(n)
print('\n')
four()
print('\n')
five()