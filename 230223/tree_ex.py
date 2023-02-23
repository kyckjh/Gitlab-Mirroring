def preorder(i):
    if i:
        print(i, end=' ')
        preorder(left[i])
        preorder(right[i])
    return
def inorder(i):
    if i:
        inorder(left[i])
        print(i, end=' ')
        inorder(right[i])
def postorder(i):
    if i:
        postorder(left[i])
        postorder(right[i])
        print(i, end=' ')



V = int(input())
arr = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)
right = [0] * (V+1)
par = [0] * (V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p
root = 1
while par[root] != 0:
    root += 1
preorder(root)
print()
inorder(root)
postorder(root)

'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''