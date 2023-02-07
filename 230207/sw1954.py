T = int(input())
for t in range(1, T+1):
    N = int(input())
    if N == 1:
        print(f'#{t}')
        print(1)
        continue
    arr = [[0]*N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = 0          
    cnt = 1
    rr = N - 1
    arr[0][0] = 1
    x, y = -1, -1
    while cnt <= N*N:
        x+=1
        y+=1
        for _ in range(4):
            for _ in range(0, rr):
                arr[y][x] = cnt
                x += dx[dir%4]
                y += dy[dir%4]
                cnt += 1
            if cnt > N*N:
                break
            dir += 1
        rr = rr - 2 if rr - 2 > 0 else 1    
    print(f'#{t}')           
    for ar in arr: 
        print(*ar)