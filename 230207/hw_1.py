T = int(input())
for t in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    for i in range(N):
        idx = i
        if i%2:
            for j in range(i, N):
                if ai[idx] > ai[j]:
                    idx = j
        else:
            for j in range(i, N):
                if ai[idx] < ai[j]:
                    idx = j
        ai[idx], ai[i] = ai[i], ai[idx]
    print(f'#{t}', end=' ')
    for i in range(10):
        print(ai[i], end=' ')
    print()
