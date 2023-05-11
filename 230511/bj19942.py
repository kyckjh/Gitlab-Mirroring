import sys
input = sys.stdin.readline

def dfs(sp, sf, ss, sv, scost, pre):
    global min_cost, min_lst
    if min_cost <= scost:
        return
    if mp <= sp and mf <= sf and ms <= ss and mv <= sv:
        min_cost = scost
        min_lst = pre
    for i in range(pre[-1]+1, N):
        dfs(sp+arr[i][0], sf+arr[i][1], ss+arr[i][2], sv+arr[i][3],scost+arr[i][4],pre+[i])

N = int(input())
mp, mf, ms, mv = map(int, input().split())
arr = []
min_cost = 10**9
min_lst = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dfs(0, 0, 0, 0, 0, [-1])

if min_cost == 10**9:
    print(-1)
else:
    print(min_cost)
    print(*list(map(lambda x: x+1, min_lst[1:])))
