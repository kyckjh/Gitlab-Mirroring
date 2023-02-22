import sys
sys.stdin = open("input.txt", "r")

def inorder(n):
    if alpha[n] == '':
        return
    inorder(tree_left[n])
    print(alpha[n], end='')
    inorder(tree_right[n])

for t in range(1, 11):
    N = int(input())
    alpha = ['']*(N+1)
    tree_left = [0]*(N+1)
    tree_right = [0]*(N+1)

    for _ in range(N):
        data = list(input().split())
        num = int(data[0])
        alpha[num] = data[1]
        if len(data) > 2:
            tree_left[num] = int(data[2])
        if len(data) > 3:
            tree_right[num] = int(data[3])
    print(f'#{t}', end=' ')
    inorder(1)
    print()
