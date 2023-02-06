arr =[ [1,2,3,4,5]
      ,[2,3,4,5,6]
      ,[3,4,5,6,7]
      ,[4,5,6,7,8]
      ,[5,6,7,8,9]
]
arr = [[x for x in range(i, i + 5)] for i in range(1, 6)]

for row in arr:
    print(row)

# 상하좌우
dy = [-1, 1, 0, 0]  # 행 변화량
dx = [0, 0, -1, 1]  # 열 변화량

#d = [(-1,0),(1,0),(0,-1),(0,1)]
#dzip = zip(dy, dx)
#print(list(dzip))

y, x = 2, 2
for i in range(4):
    print(arr[y + dy[i]][x + dx[i]])
    
r, c = 2, 2
d = [(-1,0),(1,0),(0,-1),(0,1)]
for a in range(4):
    r + d[a][0], c+d[a][1]

for dr, dc in d:
    r + dr, c + dc