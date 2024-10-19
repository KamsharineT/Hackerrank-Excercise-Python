s = set('Hackerrank')

print(s)

s.add('A')

print(s)

s.add('Hackerrank')
print(s.add('Hackerrank'))

# can not duplicate the same value in a set
s.add('Hackerrank')

print(s)

###### HAckerrank 

# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

# The first line contains an integer  N, the total number of country stamps.
N = int(input())
stampset = set()

# The next N lines contains the name of the country where the stamp is from. 
for i in range(N):
    stamps = str(input())
    stampset.add(stamps)

print(len(stampset))