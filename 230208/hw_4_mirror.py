T = int(input())
for t in range(1, T+1):
    s = input()
    mir = ''
    bdpq = ['b', 'd', 'p', 'q']
    dbqp = ['d', 'b', 'q', 'p']
    for c in s:
        mir = dbqp[bdpq.index(c)] + mir
    print(f'#{t} {mir}')