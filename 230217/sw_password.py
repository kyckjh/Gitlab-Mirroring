for t in range(1, 11):
    N, nums = input().split()
    N, nums = int(N), list(nums)
    i = 0
    while i < N-1:
        j = 0
        while i+1+j<N and nums[i-j] == nums[i+1+j]:
            j += 1
        del nums[i+1-j:i+1+j]
        i, N = i-j+1, N-j*2
    print(f'#{t} {"".join(nums)}')