# Python REgular Expressions

import re

txt = 'The Rain in Spain'

x = re.search("^The.*Spain$",txt)

if x:
    print("Found!!")

else:
    print("Not found")

# # Valid Phone number starts with 7,8 or 9 HACKERRANK
# ##########################################################################################
# n = int(input())

# for i in range(n):
#     tp = str(input())
#     if len(tp) == 10:
#         alph = re.findall("[a-zA-Z]", tp)
#         if not alph:
#             y = re.search("^7",tp) or re.search("^8",tp) or re.search("^9",tp)

#             if y :
#                 print("YES")

#             else:
#                 print("NO")
#         else:
#             print("NO")
#     else:
#         print("NO")

# #### Optimized Code for above

# import re

# # Compile regex pattern outside the loop
# pattern = re.compile(r"^[789]\d{9}$")

# n = int(input())

# for _ in range(n):
#     tp = input().strip()
#     # Check with a single regex pattern
#     if pattern.match(tp):
#         print("YES")
#     else:
#         print("NO")

##########################################################################################


## Return an empty list if no match was found:
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

##########################################################################################

# Search for the first white-space character in the string:

space = "The Singapore is Amazing"
spa = re.search("\s",space)

print("The first white-space character is located in position:",spa.start())

##########################################################################################
# Split at each white-space character:
splits = "The rain in Spain"
s = re.split("\s",splits)
print(s)

['The', 'rain', 'in', 'Spain']

str = str(input())

print(re.split("\s",str))

##########################################################################################
# Sub() ==> Replace every white-space character with the number 9:
subfn = "The Man Will Never Find"
subfn = re.sub("e","EE",subfn)

print(subfn)

# Replace the first 2 Occurrences

subfn = "The Man Will Never Find"
subfn = re.sub("e","EE",subfn,2)

print(subfn)


import re

txt = "The rain in Spain" 
x = re.search(r"\bS\w+", txt) # Print the position (start- and end-position) of the first match occurrence.
print(x.span()) # (12, 17)

ins = "The rain in Spain" 
i = re.findall('[a-c]',ins)

print(i) #['a', 'a']

x = re.findall("ai", txt)
print(x) # ['ai', 'ai']