countNum, standardNum = input().split()
standardNum = int(standardNum)
numList = map(int, input().split())
result = ''
for i in numList :
    if i < standardNum : 
        result += '{}'.format(i)
        if i+1 != int(countNum) : result += ' '
print(result)