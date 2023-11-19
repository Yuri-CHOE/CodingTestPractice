resultList = list()
for i in range(10) :
    buildingNum = int(input())
    heightList = list(map(int, input().split()))
    result = 0
    for i in range(2,buildingNum-2) :
        maxNum = max(heightList[i-2], heightList[i-1], heightList[i+1], heightList[i+2])
        if maxNum < heightList[i] : result+= heightList[i]-maxNum
    resultList.append(result)
for x in range(len(resultList)) :
    print('#{} {}'.format(x+1, resultList[x]))