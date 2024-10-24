
n = int(input())

student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

average = "{:.2f}".format(sum(student_marks[query_name])/3.00)

print(average)