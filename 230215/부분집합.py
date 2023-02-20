def f(i, k):
    if i == k:
        print(bit)
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)

A = {1,2,3}
N = len(A)
bit = [0] * N
f(0, N)
