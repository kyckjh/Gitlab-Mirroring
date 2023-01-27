from math import factorial
N = int(input())
N_fac = str(factorial(N))
result = 0
for i in range(len(N_fac)-1, -1, -1):
    if N_fac[i] == '0':
        result += 1
    else:
        break
print(result)
