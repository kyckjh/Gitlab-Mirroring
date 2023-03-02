import sys
def f(i, j, k, arr, n):
    if i == k:
        temp = []
        for ii in range(n):
            if visited[ii] == 1:
                temp.append(arr[ii])
        temp_result.append(temp)
        return
    for jj in range(j+1, n-(k-i)+1):
        visited[jj] = 1
        result = f(i+1, jj, k, arr, n)
        visited[jj] = 0



L, C = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
arr.sort()
cons = []
vowels = []
for char in arr:
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(char)
    else:
        cons.append(char)
answers = []
v_len = min(len(vowels), L-2)
for i in range(1, v_len+1):
    temp_result = []
    visited = [0] * C
    f(0, -1, i, vowels, len(vowels))
    v_result = temp_result[:]
    temp_result = []
    visited = [0] * C
    f(0, -1, L-i, cons, len(cons))
    for vs in v_result:
        for cs in temp_result:
            ans = vs+cs
            ans.sort()
            answers.append(''.join(ans))
answers.sort()
for answer in answers:
    print(answer)