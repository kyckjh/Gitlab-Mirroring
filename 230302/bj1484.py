import sys
G = int(sys.stdin.readline())
result = []
lst = [(1, G)]
n = 2
while G > n:
    if G%n == 0:
        T = G//n
        if T <= n or T == 0:
            break
        lst.append((n, T))
        n += 1
    else:
        n += 1
for sv, dv in lst:
    x = (sv+dv)/2
    if int(x) == x and dv != int(x):
        result.append(int(x))
if result:
    result.sort()
    for res in result:
        print(res)
else:
    print(-1)