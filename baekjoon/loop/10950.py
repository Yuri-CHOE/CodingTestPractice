num = int(input())
addDic = list()
for i in range(num) :
    a, b = input().split()
    addDic.append(int(a) + int(b))
for x in addDic :
    print(x)