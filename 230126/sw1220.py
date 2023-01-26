import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    arr = []
    N = int(input())
    for i in range(100):
        arr.append(list(map(int, input().split())))
    result = 0
    for i in range(100):
        temp = 0
        firstN = -1
        firstS = -1
        for j in range(100):
            if arr[j][i] == 1:
                firstN = j
                break
        for j in range(99, -1, -1):
            if arr[j][i] == 2:
                firstS = j
                break
        if firstN == -1 or firstS == -1:
            continue
        elif firstN > firstS:
            continue
        for j in range(firstN, firstS + 1):
            if arr[j][i] != 0:
                temp += 1
        result += temp
        
    print(f'#{test_case}', result)
    

# N극
# 1 : N극
# 2 : S극
# 1 : N극
# S극