max = ''
count = 0
numList = list()
for i in range(0, 9) :
    numList.append(int(input()))
for i in range(len(numList)) :
    if max == '' or numList[i] > max : 
        max=numList[i]
        count = i+1
print(max)
print(count)