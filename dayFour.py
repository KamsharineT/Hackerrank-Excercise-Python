

import itertools


# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string,
# .
# Both players have to make substrings using the letters of the string

# .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string

# .

# For Example:
# String
# = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

# Your task is to determine the winner of the game and their score.

# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

#     string string: the string to analyze

# Prints

#     string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

# Input Format

# A single line of input containing the string


######################## Google 
#   Perfect Solution :( 
#######################


def minion_gametest(string):
    s=len(string)
    vowel = 0
    consonant = 0
     
    for i in range(s):
        if string[i] in 'AEIOU':
           vowel+=(s-i)
        else:
           consonant+=(s-i)
                
    if vowel < consonant:
        print('Stuart ' + str(consonant))    
    elif vowel > consonant:
        print('Kevin ' + str(vowel))    
    else:
        print('Draw')
# how to generate random words
# if __name__ == '__main__':
#     minion_gametest("BAANANAS") 

##########################################################################
### My solution : Stupid

def minion_game(string):
    s='AEIOU'
    lists = list(s)

    substringS = []
    totS = 0
    substringK = []
    totK = 0
    #get substring of Stuart
    for i in range(len(string)):

        # loop through each ending index
        for j in range(i+1,len(string)+1):
            
            newsubstringS = string[i:j]
            if newsubstringS[0] not in lists:
                if newsubstringS not in substringS:
                    substringS.append(newsubstringS)
                    occ = string.count(newsubstringS)
                    totS = totS + occ


     #get substring of Kevin
    for i in range(len(string)):
        # loop through each ending index
        for j in range(i+1,len(string)+1):
            newsubstringK = string[i:j]
            if newsubstringK[0] in lists:
                if newsubstringK not in substringK:
                    substringK.append(newsubstringK)

                    occK = string.count(newsubstringK)
                    totK = totK + occK

    if totK > totS:                
        print ("Kevin" +" "+ str(totK))
    else:
        print ("Stuart"  +" "+ str(totS))

minion_game("BAANANAS")
##########################################################################
######### totally unwanted for this problem

def randomwords():
    # Define the letters
    letters = 'ABB'

    # Generate all unique permutations
    unique_permutations = set([''.join(p) for p in itertools.permutations(letters)])

    # Convert to a sorted list
    random_words = sorted(unique_permutations)

    # Print the random words
    for word in random_words:
        print(word)



