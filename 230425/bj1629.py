A, B, C = map(int, input().split())

d = dict()
def f(a, b, c):
    if (a, b) in d:
        return d[(a, b)]
    if b == 1:
        return a%c
    mid = b//2
    d[(a, b)] = (f(a, mid, c)*f(a, b-mid, c))%c
    return d[(a, b)]

print(f(A, B, C))