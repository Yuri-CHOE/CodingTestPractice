resultList = list()
for i in range(10) :
    num = int(input())
    resultList.append(num%42)
resultList = set(resultList)
print(len(resultList))