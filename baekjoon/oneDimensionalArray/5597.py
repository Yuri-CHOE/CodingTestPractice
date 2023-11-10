stuendentList = list()
for i in range(30) : stuendentList.append('O')
for i in range(28) : 
    tmp = int(input()) -1
    stuendentList[tmp] = 'X'
for i in range(30) :
    if stuendentList[i] == 'O' : print(i+1)