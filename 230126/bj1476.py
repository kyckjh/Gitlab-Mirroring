
# 15 28 19
# x%15 = 1 x%28 = 2 x%19 = 3
# x = 15a+1 = 29b+2 = 19c+3
# A = 15a+1
# B = 29b+2
# C = 19c+3

    
a, b, c = map(int, input().split())
i, j, k = 0, 0, 0
A, B, C = 0, 0, 0

while True:
    A = 15*i + a
    B = 28*j + b
    C = 19*k + c    
    if A == B == C:
        print(A)
        break
    if A > B:
        if B > C:
            k += 1
        else:
            j += 1
    else:
        if A > C:
            k += 1
        else:
            i += 1
    

