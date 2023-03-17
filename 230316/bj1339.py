import sys
input = sys.stdin.readline

N = int(input())
alpha = [0]*30
ALPHA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for _ in range(N):
    word = input().strip()
    word = word[::-1]
    cnt = 0
    for char in word:
        alpha[ALPHA.index(char)] += 10**cnt
        cnt += 1
alpha.sort(reverse=True)
ans = 0
for i in range(0, 9):
    ans += alpha[i]*(9-i)
print(ans)
