caseNum = int(input())
result = ''
for i in range(caseNum) :
    testNum = int(input())
    testCase = list(map(int, input().split()))
    tmpList = [0] * 101
    for i in testCase :
        tmpList[i] += 1
    maxValue = max(tmpList)
    tmp = 0
    for i in range(len(tmpList)) :
        if tmpList[i] == maxValue :
            if i > tmp : tmp = i
    result+='#{} {}\n'.format(testNum,tmp)
print(result)