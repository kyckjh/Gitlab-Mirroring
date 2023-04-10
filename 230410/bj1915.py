import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [0]*m
max_v = 0
lst = [list(map(lambda x:int(str(x)), input().strip())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i != 0 and j != 0:
            lst[i][j] += min([lst[i-1][j], lst[i][j-1], lst[i-1][j-1]])
        max_v = max(max_v, lst[i][j])
print(max_v**2)

'''
4 4
0100
0111
1111
0011

4 4
0100
0111
1111
1110



4 4
1111
0111
1110
0010



4 4
1111
1111
1111
1111



4 4
0000
0000
0000
0000



4 4
1111
1111
0000
0000


4 4
1010
0101
1010
0101


1 1
1


2 2
11
11



2 1
1
1



1 2
11
'''