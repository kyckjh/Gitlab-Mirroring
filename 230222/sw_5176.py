def inorder(n):
    global cnt
    if n > N:
        return
    inorder(n*2)
    tree[n] = cnt
    cnt += 1
    inorder(n*2+1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cnt = 1
    tree = [0]*(N+1)
    inorder(1)
    print(f'#{t} {tree[1]} {tree[N//2]}')