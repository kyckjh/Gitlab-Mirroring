def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]

queue = [0]*10

front = -1
rear = -1

rear += 1
queue[rear] = 1

enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())