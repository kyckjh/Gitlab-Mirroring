import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    H, W = map(int, input().split())
    gameMap = []
    for i in range(H):
        str_map = input()
        tempList = []
        for idx, cell in enumerate(str_map):
            tempList.append(cell)
            if cell == '^' or cell == 'v' or cell == '<' or cell == '>':
                player_x, player_y = idx, i
        gameMap.append(tempList)
        
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
            Map[y][x] = 'v'
            if y < H - 1 and Map[y+1][x] == '.':
                Map[y][x] = '.'
                Map[y+1][x] = 'v'
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
            while(0 <= tempx <= W - 1 and 0 <= tempy <= H - 1):
                if Map[y][x] == '^':
                    tempy = tempy - 1
                elif Map[y][x] == 'v':
                    tempy = tempy + 1
                elif Map[y][x] == '<':
                    tempx = tempx - 1
                elif Map[y][x] == '>':
                    tempx = tempx + 1
                if(W - 1 < tempx or tempx < 0 or H - 1 < tempy or tempy < 0):
                    break
                if Map[tempy][tempx] == '#':
                    break
                elif Map[tempy][tempx] == '*':
                    Map[tempy][tempx] = '.'
                    break
                else:
                    continue   
        return (x, y)        
        
    N = int(input())
    command = input()

    for i in range(N):
        player_x, player_y = map(int, list(Play((player_y, player_x), command[i], gameMap)))

    print(f'#{t}', end=' ')
    for h in range(H):
        for w in range(W):
            print(gameMap[h][w],end='')
        print()
            