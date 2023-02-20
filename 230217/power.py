def power(n, m):
    if m == 1: return n
    return power(n, m-1)*n

for _ in range(10):
    t = int(input())
    N, M = map(int, input().split())
    print(f'#{t} {power(N, M)}')