def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    groups = set()
    p = [x for x in range(N+1)]
    pairs = list(map(int, input().split()))
    for i in range(M):
        union(pairs[2*i], pairs[2*i+1])
    for i in range(1, N+1):
        groups.add(find_set(i))
    print(f'#{t} {len(groups)}')

'''

3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''