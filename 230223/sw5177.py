def heap_push(data):
    global last
    last += 1
    heap[last] = data
    c = last
    p = c//2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

T = int(input())
for t in range(1, T+1):
    N = int(input())
    inputs = list(map(int, input().split()))
    heap = [0]*(N+1)
    last = 0
    for data in inputs:
        heap_push(data)
    result = 0
    last //= 2
    while last > 0:
        result += heap[last]
        last //= 2
    print(f'#{t} {result}')

'''

3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''
