
queue = [None]*10
front = rear = -1

def is_empty():
    return front == rear

def is_full():
    return rear == len(queue)-1

def enQueue(data):
    global rear
    if not is_full():
        rear += 1
        queue[rear] = data
    else:
        raise IndexError('큐가 꽉 찼습니다.')

def deQueue():
    global front
    if not is_empty():
        front += 1
        return queue[front]
    else:
        raise IndexError('큐가 비었습니다.')

enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
enQueue(5)
enQueue(5)
enQueue(5)
enQueue(5)
enQueue(5)

print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
