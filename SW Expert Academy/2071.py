caseNum = int(input())
resultList = list()
for i in range(caseNum) :
    tmp = list(map(int, input().split()))
    result = 0
    for x in tmp :
        result += x
    result = round(result /len(tmp))
    resultList.append(result)

for i in range(len(resultList)) :
    print('#{} {}'.format(i+1, resultList[i]))