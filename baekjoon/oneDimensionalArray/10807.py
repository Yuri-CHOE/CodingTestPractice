countNum = int(input())
numList = map(int, input().split())
findNum = int(input())
check = 0
for i in numList :
    if findNum == i : check +=1
print(check)