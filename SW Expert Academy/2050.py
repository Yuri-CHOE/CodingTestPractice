alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
testString = input()
result = ''
for i in testString : result += '{} '.format(alpha.index(i) +1)
print(result)