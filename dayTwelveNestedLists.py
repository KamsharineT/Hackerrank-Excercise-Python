
slists = []
students = []

for _ in range(int(input())):
    scores = []

    name = input()
    score = float(input())

    # Note 1
    # scores.append(name)
    # scores.append(score)

    # slists.append(scores)

################################################################################
    # Note 1 : Do this instead
    slists.append([name,score])
################################################################################

sortedlist = sorted(slists,key= lambda x:x[1])

# print(sortedlist)

min = sortedlist[0][1]

# print(min)

## Note 2
for l in sortedlist:
    if l[1] > min:
        min = l[1]

        break

# print(min)

################################################################################
# # Note 2 : Can do this instead
# # Find the second lowest score by filtering out the minimum score

# second_min_score = next(score for name, score in sortedlist if score > min)
################################################################################

# Note 3
for student in sortedlist:
    if student[1] == min:
        students.append(student[0])

################################################################################
# # Note 3 : Do this instead
# # Collect students with the second-lowest score

# students = [name for name, score in sortedlist if score == second_min_score]
#################################################################################

s = sorted(students)

for k in s:
    print(k)