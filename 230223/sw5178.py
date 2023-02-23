def dp(i, l):
    while i != l:
        tree[i] = tree[i * 2] + tree[i * 2 + 1]
        i -= 1
    return tree[i * 2] + tree[i * 2 + 1]


T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 2)
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    print(f'#{t} {dp(N - M, L)}')