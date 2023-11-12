loopNum = int(input())
result = list()
for i in range(loopNum) :
    tmpString = input()
    result.append(tmpString[0] + tmpString[-1])
for i in result :
    print(i)