K, N = map(int, input().split())
lines = []
for k in range(K):
    lines.append(int(input()))
minK = sum(lines)//N
sum = 0
while sum != N:
    sum = 0
    for num in lines:
        sum += num // minK
    minK -= 1
print(minK + 1)

'''
4 5
10000
200
199
198
197
2000
'''