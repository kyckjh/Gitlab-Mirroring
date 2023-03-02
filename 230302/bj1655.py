def max_push(data):
    max_lst.append(data)
    idx = len(max_lst)-1
    while idx > 1:
        parent = idx//2
        if max_lst[parent] < max_lst[idx]:
            max_lst[parent], max_lst[idx] = max_lst[idx], max_lst[parent]
        else:
            break
        idx = parent
def max_pop():
    result = max_lst[1]
    max_lst[1] = max_lst.pop()
    idx = 1
    while idx < len(max_lst)-1:
        left = idx*2
        right = idx*2+1
        if left < len(max_lst):
            child = left
            if right < len(max_lst):
                if max_lst[left] < max_lst[right]:
                    child = right
            if max_lst[child] > max_lst[idx]:
                max_lst[child],  max_lst[idx] = max_lst[idx],  max_lst[child]
                idx = child
            else:
                break
        else:
            break
    return result

def min_push(data):
    min_lst.append(data)
    idx = len(min_lst) - 1
    while idx > 1:
        parent = idx // 2
        if min_lst[parent] > min_lst[idx]:
            min_lst[parent], min_lst[idx] = min_lst[idx], min_lst[parent]
        else:
            break
        idx = parent
def min_pop():
    result = min_lst[1]
    min_lst[1] = min_lst.pop()
    idx = 1
    while idx < len(min_lst)-1:
        left = idx*2
        right = idx*2+1
        if left < len(min_lst):
            child = left
            if right < len(min_lst):
                if min_lst[left] > min_lst[right]:
                    child = right
            if min_lst[child] < min_lst[idx]:
                min_lst[child],  min_lst[idx] = min_lst[idx],  min_lst[child]
                idx = child
            else:
                break
        else:
            break
    return result

import sys

N = int(sys.stdin.readline())
max_lst = [0] # 인덱스 1부터 사용
min_lst = [0]
mid = 0
for _ in range(N):
    n = int(sys.stdin.readline())
    if n > mid:
        min_push(n)
    else:
        max_push(n)
    if len(max_lst) > len(min_lst)+1:
        min_push(max_pop())
    elif len(min_lst) > len(max_lst)+1:
        max_push(min_pop())
    if len(min_lst) > len(max_lst):
        mid = min_lst[1]
    else:
        mid = max_lst[1]
    sys.stdout.write(f'{mid}\n')