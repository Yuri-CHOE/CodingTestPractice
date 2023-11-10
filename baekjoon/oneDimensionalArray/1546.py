subjectNum = int(input())
subjectScore = list(map(int, input().split()))
max = 0
total = 0
for i in subjectScore:
    if int(i) > max : max = int(i)
for i in subjectScore:
    total += i/max*100
print(total/subjectNum)
