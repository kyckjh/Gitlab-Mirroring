for t in range(1, 11):
    N, nums = input().split()
    N = int(N)
    nums = list(nums)
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
            nums.pop(i)
            i -= 1
        else:
            i += 1
    print(f'#{t} {"".join(nums)}')