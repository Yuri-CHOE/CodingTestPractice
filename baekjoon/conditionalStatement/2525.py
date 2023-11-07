hour, minute = input().split()
plus = int(input())
hour = int(hour)
minute = int(minute) + plus
if minute >= 60 :
    hour = hour + int(minute/60)
    minute = minute % 60
if hour >= 24:
    hour -= 24
print('{} {}'.format(hour, minute))

