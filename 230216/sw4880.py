def rsp(a, b):
    if arr[a] == arr[b]: return a if a < b else b
    if arr[a] + arr[b] == 4: return a if arr[a] < arr[b] else b
    return a if arr[a] > arr[b] else b

def f(start, end):
    if end == start: return start
    mid = (start+end)//2
    return rsp(f(start, mid), f(mid+1, end))

for t in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{t} {f(0, N-1)+1}')
