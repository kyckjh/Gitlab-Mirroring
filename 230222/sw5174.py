def sub_count(n):
    global ans
    if n == 0:
        return
    ans += 1
    sub_count(tree1[n])
    sub_count(tree2[n])

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree1 = [0]*(2*E)
    tree2 = [0]*(2*E)
    for i in range(E):
        if not tree1[data[i*2]]:
            tree1[data[i*2]] = data[i*2+1]
        else:
            tree2[data[i*2]] = data[i*2+1]
    ans = 0
    sub_count(N)
    print(f'#{t} {ans}')

'''

3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''