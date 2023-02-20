def enQueue(data):
    global rare
    rare += 1
    queue[rare] = data

def deQueue():
    global front
    front += 1
    return queue[front]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split())) + [None] * (M+1)
    front, rare = -1, N-1
    for _ in range(M):
        enQueue(deQueue())
    print(f'#{t} {queue[front+1]}')