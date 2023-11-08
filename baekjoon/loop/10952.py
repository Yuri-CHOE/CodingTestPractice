addList = list()
while(True) :
    a, b =input().split()
    if a == '0' and b == '0' :
        break
    addList.append(int(a) + int(b))
for i in addList :
    print(i)