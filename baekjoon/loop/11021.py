num = int(input())
addList = list()
for i in range(num) :
    a,b = input().split()
    addList.append(int(a) + int(b))
for i in range(len(addList)) :
    print('Case #{}: {}'.format(i+1,addList[i]))