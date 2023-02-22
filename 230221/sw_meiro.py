import sys
sys.stdin = open("input (2).txt", "r")

def enQueue(y, x):
    global rear
    rear += 1
    queue[rear] = (y, x)

def deQueue():
    global front
    front += 1
    return queue[front]

for _ in range(10):
    t = input()
    miro = [list(map(lambda x: int(str(x)), input().strip())) for _ in range(16)]
    # 시작점 1, 1
    cx = cy = 0
    front = rear = -1
    # 오른쪽, 아래, 왼쪽, 위
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    queue = [0]*256
    enQueue(1, 1)
    result = 0
    while front != rear:
        cy, cx = deQueue()
        if miro[cy][cx] == 3:
            result = 1
            break
        miro[cy][cx] = 1
        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]
            if miro[ny][nx] != 1:
                enQueue(ny, nx)
    print(f'#{t} {result}')

