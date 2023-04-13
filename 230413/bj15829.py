N = int(input())
alpha = input()
sum_v = 0
r = 31
M = 1234567891
for i in range(N):
    sum_v += (ord(alpha[i]) - 96)*(r**i)
print(sum_v%M)