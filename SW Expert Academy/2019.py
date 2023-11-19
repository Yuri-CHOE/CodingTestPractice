testNum = int(input())
result = '1 '
tmp = 1
for i in range(testNum) :
    tmp *=2
    result += '{} '.format(tmp)
print(result)