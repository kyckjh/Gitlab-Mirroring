import sys
sys.stdin = open("GNS_test_input.txt", "r")

num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for _ in range(T):
    t = input().split()
    num_input = input().split()
    length = len(num_input)
    for i in range(length-1):
        for j in range(0, length-1-i):
            #print(f'num_input[j] : {num_input[j]} {num_str.index(num_input[j])}')
            #print(f'num_input[j+1] : {num_input[j+1]} {num_str.index(num_input[j+1])}')
            if num_str.index(num_input[j]) > num_str.index(num_input[j+1]):
                num_input[j], num_input[j+1] = num_input[j+1], num_input[j]
    print(f'{t[0]}', end=' ')
    print(*num_input)