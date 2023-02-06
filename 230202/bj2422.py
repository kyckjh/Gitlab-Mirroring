
from math import factorial
def combination(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))

N, M = map(int, input().split())
sum = 0
nopes = list()
for m in range(M):
    a, b = map(int, input().split())
    nopes.append((a, b))

num_set = set()

for i in range(1, N - 1):
    for j in range(i + 1, N):
        for k in range(j + 1, N + 1):
            #print([i, j, k])
            num_set.add((i, j, k))

for i in range(M):
    a, b = nopes[i][0], nopes[i][1]
    #print(nopes)
    for j in range(1, N+1):
        if j != a and j != b:
            add_lst = [a, b, j]
            add_lst.sort()
            #print(num_set)
            #print(set(tuple(add_lst)))
            tempset = set()
            tempset.add(tuple(add_lst))
            #print('tempset : ', tempset)
            num_set -= tempset  # set에서 set을 빼자

#print(combination(5, 3))             
print(len(num_set))

# num1 = combination(N, 3)    # 5C3
# num2 = combination(N - 1, 2) # 4C2
# num3 = combination(N - 2, 1)

# print(num1 - num2*M + M*2 + 1)

'''
5C3
4C2 + 4C2 - M - 1

1 2
3 4
1 3

1 2 3 4 5

1 3 4
1 3 5
1 4 5

2 3 4
2 3 5
2 4 5

1 2 3
1 3 5
2 3 5

1 2 4
1 4 5
2 4 5
'''