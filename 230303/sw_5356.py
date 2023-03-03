T = int(input())
for t in range(1, T+1):
    arr = [input() for _ in range(5)]
    for i in range(len(arr)):
        arr[i] += ' '*(15-len(arr[i]))
    arr_t = list(zip(*arr))
    ans = ''
    for lst in arr_t:
        ans += "".join(lst)
    ans = ans.split()
    ans = "".join(ans)
    print(f'#{t} {ans}')

'''

2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''