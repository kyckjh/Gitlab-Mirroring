import sys

papers = [5]*5

def post(i, j, n):
    if i+n > 10 or j+n > 10 or papers[n-1] == 0:
        return False
    for y in range(i, i+n):
        for x in range(j, j+n):
            if arr[y][x] == 0:
                return False
    for y in range(i, i+n):
        for x in range(j, j+n):
            arr[y][x] = 0
    papers[n-1] -= 1
    return True

def depost(i, j, n):
    for y in range(i, i+n):
        for x in range(j, j+n):
            arr[y][x] = 1
    papers[n-1] += 1

def check(): # arr에 1이 없으면 True
    for i in range(10):
        if 1 in arr[i]:
            return False
    return True

def dfs(y, x):
    if x == 10:
        x = 0
        y += 1
    if y >= 9 and x >= 9:
        if check():
            sum = 0
            for p in papers:
                sum += p
            results.append(25-sum)
        return
    for i in range(y, 10):
        for j in range(x, 10):
            if arr[i][j] == 1:
                for n in range(5, 0, -1):
                    if post(i, j, n): # 붙이는 데 성공하면
                        print('success')
                        dfs(i, j+1)
                        depost(i, j, n)

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
results = []

# for j in range(1, 8):
#     print(post(j, 2, 1))
#     for i in range(10):
#         print(*arr[i])
# depost(2, 2, 3)
# for i in range(10):
#     print(*arr[i])
dfs(0, 0)


if results:
    print(min(results))
else:
    print(-1)

'''
0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

1 1 1 1 1 1 0 0 0 0
1 1 1 1 1 1 0 0 0 0
1 1 1 1 1 1 0 0 0 0
1 1 1 1 1 1 0 0 0 0
1 1 1 1 1 1 0 0 0 0
1 1 1 1 1 1 0 0 0 0
1 1 1 1 1 1 0 0 0 0
1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''

# def paper(lst, papers):
#     ans = 0
#     for n in range(5, 0, -1):
#         for i in range(0, 10-n+1):
#             for j in range(0, 10-n+1):
#                 for k in range(0, n):
#                     if 0 in lst[i+k][j:j+n]:
#                         break
#                 else:
#                     if papers[n] == 0:
#                         continue
#                     for y in range(0, n):
#                         for x in range(0, n):
#                             lst[i+y][j+x] = 0
#                     ans += 1
#                     papers[n] -= 1
#     for k in range(10):
#         if 1 in lst[k]:
#             return -1
#     else:
#         return ans
#
# def make_papers(i, k, lst):
#     if i == k:
#         while lst[1] != 0:
#             result = paper(copy.deepcopy(arr), copy.deepcopy(lst))
#             if result != -1:
#                 results.append(result)
#             for i in range(5, 0, -1):
#                 if lst[i] != 0:
#                     lst[i] -= 1
#                     break
#         return
#     for j in range(6):
#         make_papers(i+1, k, lst+[j])
# paperss = [5] * 6
# make_papers(0, 5, [0])
# while paperss[1] != 0:
#     result = paper(copy.deepcopy(arr), copy.deepcopy(paperss))
#     if result != -1:
#         results.append(result)
#     for i in range(5, 0, -1):
#         if paperss[i] != 0:
#             paperss[i] -= 1
#             break