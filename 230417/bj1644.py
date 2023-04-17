import sys
from collections import deque
N = int(sys.stdin.readline())
eratos = [True]*(N+1)
eratos[0] = eratos[1] = False
q = deque()
front = ans = sum_v = 0
end = 1
while front < end <= N:
    while end <= N and not eratos[end]:
        end += 1
    sum_v += end
    q.append(end)
    i = 1
    while end*i <= N:
        eratos[end*i] = False
        i += 1
    if sum_v > N:       
        while sum_v > N:
            front = q.popleft()
            sum_v -= front        
    if sum_v == N:
        ans += 1
        
print(ans)