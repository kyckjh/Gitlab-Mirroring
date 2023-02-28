for t in range(1, int(input())+1):
    _, h = input().split()
    print(f'#{t} ', end='')
    for n in h:
        for i in range(4):
            print(1 if 8 >> i & int(n, 16) else 0, end='')
    print()