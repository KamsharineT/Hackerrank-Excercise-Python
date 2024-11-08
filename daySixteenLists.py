'''Hackerrank : Basic Data Types
This is a hackerrank excercise to play with lists: 
'''

N = int(input())
listl = []

for j in range(N):
    s = str(input())
    s= s.lower()
    if 'insert' in s:
        ss = s.replace("insert","").strip()
        # print(ss)
        listl.insert(int(ss[0]),int(ss[2:]))
    elif 'print' in s:
        print(listl)
    elif 'append' in s:
        ss = s.replace("append","").strip()
        listl.append(int(ss[0:]))
    elif 'sort' in s:
        listl.sort()
    elif 'remove' in s:
        ss = s.replace("remove","").strip()
        listl.remove(int(ss[0:]))
    elif 'pop' in s:
        listl.pop()
    elif 'reverse' in s:
        listl.reverse()
print(listl)