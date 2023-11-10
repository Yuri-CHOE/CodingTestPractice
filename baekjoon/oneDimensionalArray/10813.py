basketNum, loopNum = input().split()
basketList = list()
methodList = list()
result = ''
for i in range(int(basketNum)) : basketList.append(i+1)
for i in range(int(loopNum)) : methodList.append(input())
for method in methodList :
    i,j = method.split()
    tmp = basketList[int(i)-1]
    basketList[int(i)-1] = basketList[int(j)-1]
    basketList[int(j)-1] = tmp
for x in range(len(basketList)) :
    result += '{}'.format(basketList[x])
    if x+1 != basketNum : result += ' '
print(result)