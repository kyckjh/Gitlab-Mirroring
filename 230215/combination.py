arr = [1,2,3,4,5]
N = len(arr)

selected = [0] * N
K = 3
# cnt = 여태까지 선택한 요소의 개수
def comb(idx, cnt):
    if cnt == K:
        #print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i], end=' ')
        print()
        return
    if idx == N:
        return

    for i in range(1, -1, -1):
        selected[idx] = i
        comb(idx + 1, cnt + i)


comb(0, 0)