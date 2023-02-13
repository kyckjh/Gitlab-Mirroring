import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    arr = []
    result = []
    for i in range(5):
        arr.append(list(map(str, input())))
    while arr:
        for i in range(len(arr)):
            if arr[i]:
                result.append(arr[i].pop(0))
        arr = list(filter(lambda x: len(x) != 0, arr))
    print(f'#{t} {"".join(result)}')