def enQueue(data):
    global rear
    rear = (rear+1)%10
    queue[rear] = data

def deQueue():
    global front
    front = (front+1)%10
    return queue[front]

for _ in range(10):
    t = input()
    front, rear = 0, 8
    queue = [None] + list(map(int, input().split())) + [None]
    minus = 0
    while True:
        num = deQueue() - minus % 5 - 1
        if num < 1:
            num = 0
            enQueue(num)
            break
        enQueue(num)
        minus += 1
    print(f'#{t}', end=' ')
    for i in range(front+1, front+9):
        print(queue[i%10], end=' ')
    print()