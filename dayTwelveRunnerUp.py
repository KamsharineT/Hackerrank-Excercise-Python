# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given n scores.
# Store them in a list and find the score of the runner-up. 

# Given list is [2,3,6,6,5] . The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score. 

n = int(input())
arr = map(int, input().split())

#sort the list
sortedarr = sorted(arr)

#sort the lst in desc order
sortedarre= list(reversed(sortedarr))

# find the maximum and assign it to a variable
maxm = max(sortedarre)


#iterate through the array to find the 2nd maximum
for val in sortedarre:
    if val < maxm:
        maxm = val

        #once found, break the loop
        break

print(maxm)



