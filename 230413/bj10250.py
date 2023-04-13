import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    h = (N-1)%H+1
    w = N//H+1
    if w < 10:
        print(f"{h}0{w}")
    else:
        print(f"{h}{w}")