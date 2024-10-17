
# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where K ≠ 1

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries. 
# The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of K and the room number list.

from collections import Counter

def removeKitems(roomlist,k):
    # Counter from the collections module is used to count the occurrences of each element in the list.
    # Example output for Counter : Counter({'1': 5, '2': 5, '3': 5, '6': 5, '5': 5, '4': 5, '8': 1})


    cnt = Counter(roomlist)

    print("cnt",cnt)

    # filter() combined with a lambda function is used to create a new list excluding elements that appear exactly K times. The lambda checks whether each element's count is not equal to K.
    results = list(filter(lambda x:cnt[x] != k,roomlist))

    return results
#number of members per group
K = int(input())

# room number of captain
captain = 0
# the unordered elements of the room number set.
# roomnumber = set(map(int,input().split()))

#instead get the room numbers as list
roomnumber = input().split()

# sort the list
#  (sorted(roomnumber))

captain = removeKitems(roomnumber,K)[0]
print(captain)

