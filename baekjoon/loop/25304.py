total = int(input())
productTotalNum = int(input())
sum = 0
for i in range(productTotalNum):
    productPrice, productNum = input().split()
    sum = sum + (int(productPrice) * int(productNum))
if sum == total: print('Yes')
else : print('No')