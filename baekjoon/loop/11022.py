num = int(input())
addList = list()
for i in range(num) :
    a,b = input().split()
    addList.append('Case #{}: {} + {} = {}'.format(i+1, a, b, int(a)+int(b)))
for x in addList :
    print(x)