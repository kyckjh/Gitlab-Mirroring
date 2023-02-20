def f(i, k, key):
    if i == k:
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]
        if s == key:
            return 1
        else:
            return 0
        # if s == key:
        #     for j in range(k):
        #         if bit[j]:
        #             print(A[j], end=' ')
        #     print()
    else:
        bit[i] = 1
        if f(i+1, k, key):
            return 1
        bit[i] = 0
        if f(i+1, k, key):
            return 1

A = list(range(1, 11))
bit = [0] * len(A)

print(f(0, len(A), 10))