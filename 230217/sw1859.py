# import sys
# sys.stdin = open("input1.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]

    ans = mx = 0
    for n in lst:
        if mx>n:
            ans += mx-n
        else:
            mx=n

    print(f'#{t} {ans}')