heap = [0] * (2**4)
heapcount = 0

def heap_push(data):
    global heapcount
    heapcount += 1
    heap[heapcount] = data
    parent = heapcount//2
    current = heapcount
    if heap[parent] > heap[current]:
        heap[parent], heap[current] = heap[current],  heap[parent]
        current = parent
        parent = current//2

def heap_pop():
    result = heap[1]
    heap[1] = heap[heapcount]
    heapcount -= 1
    return result

heap_push(2)
print(heap)
heap_push(3)
print(heap)
heap_push(1)
print(heap)
heap_push(5)
print(heap)
heap_push(6)
print(heap)
heap_push(7)
print(heap)