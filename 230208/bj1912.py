'''
class Save:
    def __init__(self):
        self.save_values = []
        self.keys = []

    def save_push(self, i, j, sums:int):
        if not (i, j) in self.keys:
            self.keys.append((i, j))
            self.save_values.append(sums)

    def get_save(self, i, j):
        if (i, j) in self.keys:
            return self.save_values[self.keys.index((i, j))]
        return

save = Save()
import sys
save_values = []
keys = []


def save_push(i, j, sums):
    if not (i, j) in keys:
        keys.append((i, j))
        save_values.append(sums)

def get_save(i, j):
    if (i, j) in keys:
        return save_values[keys.index((i, j))]
    return


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def sum_arr(from_n, to_n):
    result = get_save(from_n, to_n)
    sums = 0
    #print(result)
    if result:  # result != None
        return result
    else:
        if to_n - from_n < 2:
            sums += sum(nums[from_n:to_n])
        else:
            mid = (from_n + to_n)//2
            sums += sum_arr(from_n, mid) + sum_arr(mid, to_n)
    #if from_n - to_n > 10:
    save_push(from_n, to_n, sums)
    return sums

results = []
for k in range(1, N + 1):
    for i in range(N-k+1):
        #print(f'{i}, {i+k} : {sum_arr(i, i+k)}')
        results.append(sum_arr(i, i+k))
print(max(results))
'''

import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

maxSum = nums[0]
for i in range(0, N+1):
    tempSum = 0
    for j in range(i, N):
        tempSum += nums[j]
        if maxSum < tempSum:
            maxSum = tempSum
print(maxSum)