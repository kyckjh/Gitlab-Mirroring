import sys
sys.stdin = open("input4.txt", "r")

T = int(input())
for t in range(1, T+1):
    fac = 362880
    result = 1
    arr = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        set1 = set()
        set2 = set()
        for j in range(9):
            set1.add(arr[i][j])
            set2.add(arr[j][i])
        if len(set1) != 9:
            result = 0
            break
        if len(set2) != 9:
            result = 0
            break
    delta = [[i, j] for j in range(3) for i in range(3)]
    #delta = [[0, 0],[0, 1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    if result:
        for x, y in delta:
            set3 = set()
            for i, j in delta:
                set3.add(arr[x*3+i][y*3+j])
            if len(set3) != 9:
                result = 0
                break
    print(f'#{t} {result}')