import sys
input = sys.stdin.readline
N = int(input())
# arr : 풍선에 적힌 번호들
arr = list(map(int, input().split()))
# arr에 풍선의 처음 순서 번호 함께 저장
for i in range(N):
    arr[i] = (i+1, arr[i])
idx = 0
ans = []
while True:
    temp = arr.pop(idx) # 풍선 터뜨리면서 arr에서 빼기
    ans.append(temp[0]) # 풍선의 번호를 ans배열에 순서대로 추가
    next = temp[1]-1    # 다음 터뜨릴 풍선의 번호
    N -= 1  # 총 풍선 개수 줄이기
    if N == 0:  # 풍선이 다 터지면 끝내기
        break
    if next < 0:    # 풍선에 음수가 적혀있었을 때는 앞으로 next+1번 가야 됨
        next += N+1 # 앞으로 next+1번 가기 = 뒤로 next+N+1번 가기
    idx = (idx+next)%N   # idx가 배열 인덱스 범위 벗어나지 않도록 모듈러연산
print(*ans)