import sys
sys.stdin = open("sample_input (1).txt", "r")

def enQueue(y, x, d):
    global rear
    rear += 1
    queue[rear] = (y, x, d)

def deQueue():
    global front
    front += 1
    return queue[front]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    miro = [list(map(lambda x: int(str(x)), input().strip())) for _ in range(N)]
    cx = cy = 0
    cd = -2 # 거리 (출발점과 도착점을 뺀 거리라서 -2)
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                cy, cx = i, j
                break
        else:
            continue
        break
    front = rear = -1
    # 오른쪽, 아래, 왼쪽, 위
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    queue = [0]*(N*N)
    enQueue(cy, cx, cd)
    while True:
        if front == rear:
            cd = 0
            break
        cy, cx, cd = deQueue()
        cd += 1
        if miro[cy][cx] == 3:
            break
        miro[cy][cx] = 1
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0 <= ny < N and 0 <= nx < N and miro[ny][nx] != 1:
                enQueue(ny, nx, cd)
    print(f'#{t} {cd}')

