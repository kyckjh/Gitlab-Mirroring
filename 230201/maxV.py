'''
3
5
5 7 78 12 42
6
4 9 13 5 44 91
7
19 10 2 44 72 33 41
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[0]   # 첫 원소를 최대로 가정
    for i in range(1, N):    # 나머지 원소와 비교
        if maxV < arr[i]:
            maxV = arr[i]
    print(f'#{tc} {maxV}')