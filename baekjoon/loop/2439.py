num = int(input())
str = '*'
str2 = ' '
for i in range(1,num+1) :
    print('{}{}'.format(str2*(num-i),str*i))
    #print('{}'.format(str*i).rjust(num))5