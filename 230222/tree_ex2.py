def preorder(T):
    if T >= 2 ** 4 or tree[T] == '':
        return
    print(tree[T], end=' ')
    preorder(T*2)
    preorder(T*2+1)

tree = ['']*2**4
N = int(input())
data = list(input().split())
for i in range(N):
    tree[int(data[2*i])] = data[2*i+1]
preorder(1)
'''
9
1 a 2 b 3 c 4 d 5 e 6 f 7 g 10 h 14 i
'''