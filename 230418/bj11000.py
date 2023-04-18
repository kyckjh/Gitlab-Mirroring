N = int(input())
ss = []
tt = []
for _ in range(N):
    s, t = map(int, input().split())
    ss.append(s)
    tt.append(t)

ss.sort()
tt.sort()
cnt = ans = 0
for i in range(N):
    if ss[i] >= tt[cnt]:
        cnt += 1
    else:
        ans += 1

print(ans)

'''
8
1 8
9 16
3 7
8 10
10 14
5 6
6 11
11 12

답 : 3

'''