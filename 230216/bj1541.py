import sys

def f(i, k):
    global minSum

    if i == k:
        tempSum = 0
        for j in range(0, N):
            if p[j] == 1:
                tempSum -= nums[j]
            else:
                tempSum += nums[j]
        if minSum > tempSum:
            minSum = tempSum
    for j in range(i, N):
        p[j] = 1
        f(i+1, k)
        p[j] = 0




inputs = sys.stdin.readline()

num = 0
nums = []
plus = 0 # 더하기 개수
minus = 0
for char in inputs:
    if char == '+':
        plus += 1
        nums.append(num)
        num = 0
    elif char == '-':
        minus += 1
        nums.append(num)
        num = 0
    elif char != '\n':
        num = num*10 + int(char)
else:
    nums.append(num)

minSum = 99999999

N = plus + minus + 1
p = [0] * N
f(0, minus)
print('minus', minus)
print(minSum)