import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = tuple(map(int, input().split()))
arr.sort()  # 먼저 시작 시간을 기준으로 정렬하여 다음 정렬에서 시작 시간도 정렬되어 있도록 함
arr.sort(key=lambda x:x[1]) # 끝나는 시간을 기준으로 정렬
last = -1   # 이전 회의가 끝난 시간을 저장할 변수, 회의 시작 시간이 0부터 시작하므로 0 미만으로 초기화
ans = 0     # 회의의 최대 개수
for start, end in arr:  # 회의 시간 순서대로 순회
    if last > start:    # 저번 회의가 끝난 시간이 이번 회의의 시작시간보다 늦으면
        continue        # 시간이 겹치므로 cotinue
    last = end          # 시간이 겹치지 않으면 회의 끝난 시간 업데이트
    ans += 1            # 회의 개수 증가
print(ans)