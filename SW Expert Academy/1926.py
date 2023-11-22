testNum = int(input())
result = ''
for i in range(1,testNum+1) :
    strI = str(i)
    if '3' in strI or '6' in strI or '9' in strI : 
        count = 0
        count += strI.count('3')
        count += strI.count('6')
        count += strI.count('9')
        print('count : {}'.format(count))
        result = result + ('-'*count)
    else :
        result += strI
    result += ' '
print(result)       