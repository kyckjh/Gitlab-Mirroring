def bi(n, i, result):
    if i > 12:
        print('overflow')
        return
    now = pow(2, -i)
    if n > now:
        n -= now
        bi(n, i+1, result + '1')
    elif n == now:
        print(result + '1')
    else:
        bi(n, i+1, result + '0')

T = int(input())
for t in range(1, T+1):
    N = float(input())
    print(f'#{t}', end=' ')
    bi(N, 1, '')