import sys
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    s = sys.stdin.readline().split(',')
    set1 = set()
    for ss in s:
        if '-' in ss:
            a, b = map(int, ss.split('-'))
            for i in range(a, b+1):
                if i > N:
                    break
                set1.add(i)
        else:
            a = int(ss)
            if a <= N:
                set1.add(a)
    print(len(set1))
