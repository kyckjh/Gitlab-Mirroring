def f(i, k, s, t):
    global cnt
    global fcnt
    fcnt += 1
    if s > t: # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    if i == k:
        if s == t:
            # for j in range(k):
            #     if bit[j]:
            #         print(A[j], end=' ')
            # print(':', t)
            cnt += 1
        return
    else:
        #bit[i] = 1
        f(i+1, k, s+A[i], t)
        #bit[i] = 0
        f(i+1, k, s, t)
fcnt = 0
A = list(range(1, 21))
N = len(A)
key = 10
cnt = 0
bit = [0]*N
f(0, N, 0, key)
print(cnt, fcnt)