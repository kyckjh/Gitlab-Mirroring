import sys
sys.stdin = open("input.txt", "r")

T = int(input())
H, W = map(int, input().split())

print(T, H, W)

gameMap = []
for i in range(H):
    str_map = input()
    tempList = []
    for cell in str_map:
        tempList.append(cell)
    gameMap.append(tempList)
print(gameMap)
    
def Play(player, command, Map):
    x = player[1]
    y = player[0]
    if command == 'U':
        Map[y][x] = '^'
        if y > 0 and Map[y-1][x] == '.':
            Map[y][x] = '.'
            Map[y-1][x] = '^'
    if command == 'D':
        Map[y][x] = 'V'
        if y < H - 1 and Map[y+1][x] == '.':
            Map[y][x] = '.'
            Map[y-1][x] = 'V'
    if command == 'L':
        Map[y][x] = '<'
        if x > 0 and Map[y][x-1] == '.':
            Map[y][x] = '.'
            Map[y-1][x] = '<'
    if command == 'R':
        Map[y][x] = '>'
        if x < W - 1 and Map[y][x+1] == '.':
            Map[y][x] = '.'
            Map[y-1][x] = '>'
    if command == 'S':
        pass
        
    
N = int(input())
command = input()

for i in range(N):
    for j in range(H):
        for k in range(W):
            if gameMap[j][k] == '^' or gameMap[j][k] == 'V' or gameMap[j][k] == '<' or gameMap[j][k] == '>':
                Play((j, k), command[i], gameMap)  