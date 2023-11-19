caseNum = int(input())
resultList = list()
for i in range(caseNum) :
    a, b = map(int, input().split())
    result = [int(a/b), a%b]
    resultList.append(result)
for i in range(len(resultList)) :
    print('#{} {} {}'.format(i+1, resultList[i][0], resultList[i][1]))