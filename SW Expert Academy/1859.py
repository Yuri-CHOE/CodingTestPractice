caseNum = int(input())
result = ''
for x in range(caseNum) :
    dayNum = int(input())
    priceList = list(map(int, input().split()))
    tmp = 0
    sellPrice = 0
    for i in priceList[::-1] :
        if i >= sellPrice : sellPrice=i
        else : tmp += sellPrice-i
    result += '#{} {}\n'.format(x+1, tmp)
print(result)