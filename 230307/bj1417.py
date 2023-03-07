N = int(input())
arr = [int(input()) for _ in range(N)]
one = arr[0]
ans = 0
while True:
    one = arr[0]
    max_v = one
    max_idx = 0
    for i in range(len(arr)):
        if max_v <= arr[i]:
            max_v = arr[i]
            max_idx = i
    if max_idx == 0:
        break
    arr[max_idx] -= 1
    arr[0] += 1
    ans += 1
print(ans)