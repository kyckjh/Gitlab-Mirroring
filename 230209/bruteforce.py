p = 'ab'
t = 'aaaabaaaabaaaab'

def bf(p, t, N, M):
    i = 0   # t 에서의 비교위치
    j = 0   # p 에서의 비교위치
    while i < N and j < M:  # 비교할 문장이 남아있고, 패턴을 찾기 전이면
        if t[i] != p[j]:    # 다른 글자를 만나면
            i -= j          # 비교를 시작한 위치로
            j = -1          # 패턴의 시작 전으로
        i += 1
        j += 1
    if j == M:  # 패턴을 찾은 경우
        return i - M
    else:
        return -1

def bf2(p, t, N, M):
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            cnt += 1
    return cnt

print(bf(p, t, len(t), len(p)))
print(bf2(p, t, len(t), len(p)))



