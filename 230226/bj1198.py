import sys
def triangle(i, j, k):
    a, d = arr[i]
    b, e = arr[j]
    c, f = arr[k]
    first = (a*e)+(b*f)+(c*d)
    second = (d*b)+(e*c)+(f*a)
    area = (first-second)*0.5
    return area*-1 if area < 0 else area


N = int(sys.stdin.readline())
arr = [0]*N
max_ans = 0
for i in range(N):
    arr[i] = tuple(map(int, sys.stdin.readline().split()))
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = triangle(i, j, k)
            if max_ans < temp:
                max_ans = temp
print(max_ans)
