# You are given n words. Some words may repeat. For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word. 


# Input Format

# The first line contains the integer n.
# The next n lines each contain a word. 


# This line reads an integer input from the user, which is stored in the variable n. This value represents how many strings will be inputted next.
n = int(input())

# An empty dictionary strings is initialized. This dictionary will store each unique string as a key, and the value will be a list of positions where that string appeared (1-based index).
strings = {}

for i in range(n):
    string = input()

#  This checks if the current string (stored in string) already exists as a key in the strings dictionary.
    if string in strings:

# If the string already exists in the dictionary, the position (i+1) is appended to the list of positions for that string. i+1 is used because we want to track positions starting from 1, not 0 (since i starts from 0).
        strings[string].append(i+1)

#  If the string is not already in the dictionary, a new entry is created where the key is the string, and the value is a list containing the current position (i+1).
    else:
        strings[string] = [i+1]

print(len(strings))
for key, value in strings.items():
    print(len(value), end=" ")
