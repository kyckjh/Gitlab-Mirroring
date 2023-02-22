import sys

def make(i, j, digit_str, n):
    if i < 0 or j < 0 or i > 4 or j > 4:
        return
    if n == 0:
        result_set.add(digit_str+data[i][j])
        return
    for k in range(4):
        make(i+dy[k], j+dx[k], digit_str+data[i][j], n-1)

data = [list(sys.stdin.readline().split()) for _ in range(5)]
result_set = set()
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
for i in range(5):
    for j in range(5):
        make(i, j, '', 5)
print(len(result_set))