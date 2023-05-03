n = int(input())
fives = n//5
remain = n%5
while fives > 0:
    if not remain%2:
        break
    fives -= 1
    remain = n - 5*fives
if remain%2:
    print(-1)
else:
    print(fives+remain//2)