import sys
sys.stdin = open("sample_input(1).txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 2) for _ in range(N + 2)]
    mid = N // 2
    arr[mid][mid] = arr[mid + 1][mid + 1] = 2
    arr[mid + 1][mid] = arr[mid][mid+1] = 1

    for _ in range(M):
        y, x, wb = map(int, input().split())
        arr[y][x] = wb
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i, j in dirs:
            di, dj = y+i, x+j
            cnt = 0
            while arr[di][dj]:
                if arr[di][dj] == wb:
                    while cnt > 0:
                        di -= i
                        dj -= j
                        cnt -= 1
                        arr[di][dj] = wb
                    break
                else:
                    cnt += 1
                    di += i
                    dj += j
    black = 0
    white = 0
    for lst in arr:
        black += lst.count(1)
        white += lst.count(2)
    print(f'#{t} {black} {white}')

'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''