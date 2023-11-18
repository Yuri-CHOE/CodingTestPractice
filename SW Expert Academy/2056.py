caseNum = int(input())
monthDay = [31,28,31,30,31,30,31,31,30,31,30,31]
resultList = list()
for i in range(caseNum) :
    tmp = False
    result = input()
    if int(result[4:6]) >= 1 and int(result[4:6])  <= 12 :
        if int(result[6:]) >=1 and int(result[6:])  <= monthDay[int(result[4:6])-1] : tmp = True
    if tmp :
        resultList.append('{}/{}/{}'.format(result[:4],result[4:6],result[6:]))
    else :
        resultList.append('-1')

for i in range(len(resultList)) :
    print('#{} {}'.format(i+1, resultList[i]))