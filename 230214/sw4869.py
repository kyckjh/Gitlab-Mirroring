def paper(n):
    p = [0] * (n+1)
    p[0] = 1
    p[1] = 3
    for i in range(2, n):
        p[i] = p[i-1] + 2*p[i-2]
    return p[n-1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = paper(N//10)
    print(f'#{t} {ans}')