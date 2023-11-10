countNum, standardNum = input().split()
standardNum = int(standardNum)
numList = list(map(int, input().split()))
for i in range(int(countNum)) :
    if numList[i] < standardNum :     
        print(numList[i], end=' ')