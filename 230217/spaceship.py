import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    arr = [[10]*(M+2)]
    for _ in range(N):
        arr.append([10]+list(map(int, input().split()))+[10])
    arr.append([10]*(M+2))

    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # for i in range(N+2):
    #     print(arr[i])

    for i in range(1, N+1):
        for j in range(1, M + 1):
            now = arr[i][j]
            can = 0
            for y, x in dirs:
                if arr[i+y][j+x] < now:
                    can += 1
            if can > 3:
                ans += 1

    print(f'#{t} {ans}')