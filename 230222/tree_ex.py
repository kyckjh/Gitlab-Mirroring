'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

'''

V = int(input())
tree = [[0] * (V+1) for _ in range(2)]
data = list(map(int, input().split()))

def preorder(T):
    if T == 0:
        return
    print(T, end=' ')
    preorder(tree[0][T])
    preorder(tree[1][T])

def inorder(T):
    if T == 0:
        return
    inorder(tree[0][T])
    print(T, end=' ')
    inorder(tree[1][T])

def postorder(T):
    if T == 0:
        return
    postorder(tree[0][T])
    postorder(tree[1][T])
    print(T, end=' ')

for i in range(0, (V-1)*2, 2):
    p, c = data[i], data[i+1]
    if not tree[0][p]:
        tree[0][p] = c
    else:
        tree[1][p] = c

preorder(1)
print()
inorder(1)
print()
postorder(1)
