import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = N-1
ans = 0
pre_diff = 0xffffffff
min_diff = 0xffffffff
while left != right:
    diff = abs(arr[left]+arr[right])
    if diff < min_diff:
        min_diff = diff
        ans = (left, right)
    if diff > pre_diff:
        left += 1        
        right += 1
        pre_diff = 0xffffffff
    else:
        pre_diff = diff
        right -= 1
print(arr[ans[0]], arr[ans[1]])