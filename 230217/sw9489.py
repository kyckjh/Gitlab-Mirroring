import sys
sys.stdin = open("input1.txt", "r")

def count(arr):
    mx = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n==1:
                cnt += 1
                if mx<cnt:
                    mx = cnt
            else:
                cnt = 0
    return mx

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))

    ans = count(arr)
    ans2 = count(arr_t)
    if ans<ans2:
        ans=ans2

    print(f'#{t} {ans}')