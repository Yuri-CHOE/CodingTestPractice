subjectNum = int(input())
subjectScore = map(int, input().split())
max = 0
total =0
for i in subjectScore:
    if int(i) > max : max = int(i)
print(max)
for i in subjectScore:
    print(i)
    total = total + (int(i)/max*100)
    print(total)
print(total/subjectNum)
