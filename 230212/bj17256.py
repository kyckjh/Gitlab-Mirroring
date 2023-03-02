import sys

a = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

print(f'{c[0] - a[2]} {c[1]//a[1]} {c[2]-a[0]}')
