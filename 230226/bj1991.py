import sys
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def pre(i):
    if i == -1:
        return
    print(alpha[i], end='')
    pre(left[i])
    pre(right[i])

def post(i):
    if i == -1:
        return
    post(left[i])
    post(right[i])
    print(alpha[i], end='')

def inorder(i):
    if i == -1:
        return
    inorder(left[i])
    print(alpha[i], end='')
    inorder(right[i])

N = int(sys.stdin.readline())
left = [-1]*N
right = [-1]*N
for i in range(N):
    p, l, r = map(str, sys.stdin.readline().split())
    if l != '.':
        left[alpha.index(p)] = alpha.index(l)
    if r != '.':
        right[alpha.index(p)] = alpha.index(r)
pre(0)
print()
inorder(0)
print()
post(0)
