import sys
order = [0]*9
order[3] = 1
c = [0]*9
c[3] = 1
max_score = 0
def perm(cnt):
    global max_score
    if cnt == 10: # 순열 완성
        now = score = 0
        for inn in arr: # n : 현재 이닝
            out = b1 = b2 = b3 = 0
            while out < 3:
                player = inn[order[now]-1]
                if player == 0:
                    out += 1
                elif player == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif player == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif player == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                else:
                    score += b1+b2+b3+1
                    b1 = b2 = b3 = 0
                now = (now+1)%9
        max_score = max(score, max_score)
        return
    for i in range(9):
        if c[i]:
            continue
        c[i] = 1
        order[i] = cnt
        perm(cnt + 1)
        c[i] = 0
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
perm(2)
print(max_score)