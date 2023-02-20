N = 3
arr = [1,2,3]
perm_arr = [0] * N
used = [0] * N
# idx 번째에 넣을 수 있는 숫자 다 넣기
def perm(idx):
    if idx == N:
        print(perm_arr)
        return
    for i in range(N):
        if not used[i]:
            perm_arr[idx] = arr[i]
            used[i] = 1
            perm(idx + 1)
            used[i] = 0

perm(0)