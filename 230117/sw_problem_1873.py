import sys
sys.stdin = open("input.txt", "r")

T = int(input())
H, W = map(int, input().split())

print(T, H, W)

gameMap = []

for i in range(H):
    str_map = input()
    tempList = []
    for idx, cell in enumerate(str_map):
        tempList.append(cell)
        if cell == '^' or cell == 'V' or cell == '<' or cell == '>':    # 현재 플레이어 위치 확인
            player_x, player_y = idx, i
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
            y = y-1
    elif command == 'D':
        Map[y][x] = 'V'
        if y < H - 1 and Map[y+1][x] == '.':
            Map[y][x] = '.'
            Map[y+1][x] = 'V'
            y = y+1
    elif command == 'L':
        Map[y][x] = '<'
        if x > 0 and Map[y][x-1] == '.':
            Map[y][x] = '.'
            Map[y][x-1] = '<'
            x = x-1
    elif command == 'R':
        Map[y][x] = '>'
        if x < W - 1 and Map[y][x+1] == '.':
            Map[y][x] = '.'
            Map[y][x+1] = '>'
            x = x+1
    elif command == 'S':
        tempx = x
        tempy = y
        while(0 < tempx < W - 1 and 0 < tempy < H - 1):
            if Map[tempy][tempx] == '^':
                tempy = tempy + 1
            elif Map[tempy][tempx] == 'V':
                tempy = tempy - 1
            elif Map[tempy][tempx] == '<':
                tempx = tempx - 1
            elif Map[tempy][tempx] == '>':
                tempx = tempx + 1
                
            if Map[tempy][tempx] == '#':
                break
            elif Map[tempy][tempx] == '*':
                Map[tempy][tempx] = '.'
                break
            elif Map[tempy][tempx] == '_' or Map[tempy][tempx] == '.':
                continue   
    return (x, y)
        
    
N = int(input())
command = input()

for i in range(N):
    player_x, player_y = map(int, list(Play((player_y, player_x), command[i], gameMap)))
    print(command[i])
    for cells in gameMap:
        print(cells)
    print('====================')