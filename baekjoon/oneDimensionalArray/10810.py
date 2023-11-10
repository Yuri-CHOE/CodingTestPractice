basketNum, loopNum = input().split()
basketList = list()
methodList = list()
result = ''
for i in range(int(basketNum)) : basketList.append(0)
for i in range(int(loopNum)) : methodList.append(input())
for method in methodList :
    i,j,k = method.split()
    for y in range(int(i)-1, int(j)) :
        basketList[y] = int(k)
for x in range(len(basketList)) :
    result += '{}'.format(basketList[x])
    if x+1 != basketNum : result += ' '
print(result)