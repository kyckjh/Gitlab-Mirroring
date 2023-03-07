def dfs(current, change_cnt, battery):
    global best
    if battery < 0:
        return
    if current == N-1:
        best = min(best, change_cnt)
        return
    if change_cnt >= best:
        return
    if battery < M[current]:
        dfs(current+1, change_cnt+1, M[current]-1)    
    dfs(current+1, change_cnt, battery-1)

T = int(input())
for t in range(1, T+1):
    best = 101
    N, *M = map(int, input().split())
    dfs(0, 0, M[0])
    print(f'#{t} {best}')