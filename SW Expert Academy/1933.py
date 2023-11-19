testNum = int(input())
result = ''
for i in range(1, testNum + 1) :
    if testNum % i == 0 : result += '{} '.format(i)
print(result)
