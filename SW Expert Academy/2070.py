caseNum = int(input())
resultList = list()
for i in range(caseNum) :
    tmp = list(map(int, input().split()))
    result = 0
    if tmp[0] == tmp[1] : result = '='
    elif tmp[0] > tmp[1] : result = '>'
    else : result = '<'
    resultList.append(result)

for i in range(len(resultList)) :
    print('#{} {}'.format(i+1, resultList[i]))