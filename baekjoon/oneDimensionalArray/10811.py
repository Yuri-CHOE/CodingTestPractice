basketNum, loopNum = input().split()
basketList = list()
result = ''
for i in range(int(basketNum)) : basketList.append(i+1)
for i in range(int(loopNum)) : 
    i,j = map(int, input().split())
    tmp = basketList[i-1:j]
    tmp = reversed(tmp)
    basketList[i-1:j] = tmp
for x in basketList :
    print(x, end=' ')