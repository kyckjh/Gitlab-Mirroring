import sys
input = sys.stdin.readline

# num_lst : 반전된 숫자, cnt : 반전된 LED의 개수, depth : 반전할 자릿수
def dfs(num_lst, cnt, depth):
    global ans
    if cnt > P: # 반전된 LED의 개수가 P를 넘어가면 반환
        return
    if depth >= K:  # 모든 자리를 바꿨을 때
        if 1 <= int("".join(num_lst)) <= N: # 바꾼 숫자가 1 이상 N 이하이면
            ans += 1    # 정답 경우의 수 1 증가
        return
    for i in range(10): # 해당 자릿수를 0부터 9까지로 반전
        diff = nums[i]^nums[X[depth]] # 원래 숫자와 바꾼 숫자의 LED에서 다른 부분 XOR 연산
        add_cnt = str(bin(diff)).count('1') # 반전한 LED의 개수
        num_lst[depth] = str(i) # 숫자 바꾸기
        dfs(num_lst, cnt+add_cnt, depth+1)  # 다음 자릿수 바꾸기
    num_lst[depth] = '0'    # 숫자 되돌리기


N, K, P, X = map(int, input().split())
nums = [0b1110111, 0b0000011, 0b0111110, 0b0011111, 0b1001011, 0b1011101, 0b1111101, 0b0010011, 0b1111111, 0b1011111]
X = list(str(X))
X = [0]*(K-len(X))+list(map(int, X))
ans = 0
dfs(['0']*K, 0, 0)
print(ans-1)