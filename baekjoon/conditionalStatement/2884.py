a, b = input().split()
a = int(a)
b = int(b)
if b < 45 :
    a -= 1
    b += 60
if a < 0 :
    a += 24
print('{} {}'.format(a,b-45))
