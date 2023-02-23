def enq(n):
    heap.append(n)
    c = len(heap)-1
    p = c//2
    # 부모가 있고, 부모 > 자녀
    while p>0 and abs(heap[p]) >= abs(heap[c]):
        if abs(heap[p]) == abs(heap[c]):
            if heap[p] < heap[c]:
                break
        heap[p], heap[c] = heap[c], heap[p]
        c = p       # 옮긴 자리에서 부모와 비교하기 위해
        p = c//2
    return

def deq():
    if len(heap) == 2:
        return heap.pop()
    elif len(heap) == 1:
        return 0
    tmp = heap[1]           # 루트 임시저장
    heap[1] = heap.pop()   # 마지막 정점의 값을 루트로 이동
    last = len(heap)-1       # 마지막 정점 삭제
    p = 1
    c = p*2                 # 왼쪽자식번호
    while c <= last:        # 자식이 하나 이상 있으면
        # 오른쪽 자식이 있고, 오른쪽 자식의 key가 더 크면
        if c+1 <= last and abs(heap[c]) >= abs(heap[c+1]):
            if abs(heap[c]) == abs(heap[c+1]):
                if heap[c] > heap[c+1]:
                    c += 1
            else:
                c += 1          # 비교 대상을 오른쪽 자식으로 변경
        if abs(heap[c]) <= abs(heap[p]):  # 자식이 부모보다 크면
            if abs(heap[p]) == abs(heap[c]):
                if heap[p] < heap[c]:
                    break
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p*2
        else:
            break
    return tmp

heap = [0]
import sys
N = int(sys.stdin.readline())
for _ in range(N):
    order = int(sys.stdin.readline())
    if not order:
        print(deq())
    else:
        enq(order)