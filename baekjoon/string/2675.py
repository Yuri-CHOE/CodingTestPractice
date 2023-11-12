loopNum = int(input())
result = list()
for i in range(loopNum) :
    r, string = input().split()
    tmp = ''
    for i in string :
        tmp += i *int(r)
    result.append(tmp)
for i in result :
    print(i)