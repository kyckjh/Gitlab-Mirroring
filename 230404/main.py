import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    heapq.heappush(q, int(input()))
sum_v = 0

while q and q[0] < 0:
    a = heapq.heappop(q)
    if q and q[0] < 0:
        b = heapq.heappop(q)
    else:
        if q and q[0] == 0:
            break
        else:
            sum_v += a
            break
    sum_v += a*b
while q and q[0] == 0:
    heapq.heappop(q)
while (q and q[0] == 1) or len(q)%2:
    sum_v += heapq.heappop(q)
while q:
    sum_v += heapq.heappop(q) * heapq.heappop(q)
print(sum_v)