alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
string = input()
result = 0
for i in string :
    for x in alphabet :
        if i in x :
            tmp= int(alphabet.index(x)) +3
            result += tmp
            break
print(result)