
import sys
sys.stdin = open("input_04.txt", "r")

T = 10
for t in range(1, T+1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 100*100
    for sj in range(1, 101):
        si = 0
        if arr[si][sj] != 1:
            continue
        cnt, dj = 0, 0
        ci, cj = si, sj
        while ci < 99:
            if dj == 0:
                if arr[ci][cj-1] == 1:
                    dj = -1
                    cj += dj
                elif arr[ci][cj+1] == 1:
                    dj = 1
                    cj += dj
                else:
                    while not (arr[ci][cj-1] or arr[ci][cj+1]) and ci < 99:
                        ci += 1
                        cnt += 1
            else:
                while arr[ci][cj + dj]:
                    cj += dj
                    cnt += 1
                dj = 0
                ci += 1
            cnt += 1
        if mn >= cnt:
            mn, ans = cnt, sj - 1
    print(f'#{t} {ans}')
