countNum = int(input())
numLIst = map(int,input().split())
max = -1000000
min = 1000000
for i in numLIst :
    if i > max : max = i
    if i < min : min = i
print('{} {}'.format(min, max))