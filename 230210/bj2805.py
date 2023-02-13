import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)
mid = end//2
while start < end:
    sum = 0
    for n in list(filter(lambda x : x > mid, arr)):
        #print(n, mid)
        sum += n - mid
    if sum > M:
        start = mid + 1
    elif sum < M:
        end = mid - 1
    else:
        break
    mid = (start + end)//2

sum = 0
arr = list(filter(lambda x : x > mid, arr))
for n in arr:
    sum += n - mid
if sum < M:
    while sum < M:
        sum = 0
        #print(mid)
        mid-=1
        for n in arr:
            sum += n - mid
    print(mid)
elif sum > M:
    while sum > M:
        sum = 0
        #print(arr, sum, mid)
        mid += 1
        for n in arr:
            sum += n - mid
    print(mid - 1)
else:
    print(mid)

'''
4 7
20 16 10 17

'''