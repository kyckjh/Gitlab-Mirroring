import sys
input = sys.stdin.readline

def dis(a, b):
    return (abs(arr[a][0]-arr[b][0])**2 + abs(arr[a][1]-arr[b][1])**2)**0.5

n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(float, input().split())))

mst = set()
mst.add(0)
ans = 0
while len(mst) < n:
    min_v = 10**8
    for now in mst:
        for i in range(n):
            if i in mst:
                continue
            dist = dis(now, i)
            if dist < min_v:
                min_v = dist
                next = i
    ans += min_v
    mst.add(next)
print(ans)