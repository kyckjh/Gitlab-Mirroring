def power(n, m):
    if m == 1:
        return n
    return power(n, m-1) * n

for _ in range(10):
    t = input()
    n, m = map(int, input().split())
    ans = power(n, m)
    print(f'#{t} {ans}')