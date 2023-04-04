


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    q.append((N, 0))
    check = set()
    while q:
        now, cnt = q.popleft()
        if now in check:
            continue
        check.add(now)
        if now == M:
            break
        for d in [1, -1, now, -10]:
            if 0 <= now+d <= 1000000:
                q.append((now+d, cnt+1))
    print(f'#{t} {cnt}')