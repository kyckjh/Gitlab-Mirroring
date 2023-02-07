def g(N):
    sum = 0
    for i in range(1, N-2):
        sum += i * (N - 2 - i)
    return sum

def f(N):
    if N == 4:
        return 1
    elif N < 4:
        return 0
    return f(N-1) + g(N)

n = int(input())

print(f(n))