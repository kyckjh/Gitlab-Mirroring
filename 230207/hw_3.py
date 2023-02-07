import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    destination = 0
    for i in range(100):
        if data[99][i] == 2:
            destination = i
    nowy = 99
    nowx = destination
    while nowy > 0:
        if nowx < 99:
            if data[nowy][nowx + 1] == 1:
                nowx += 1
                while data[nowy-1][nowx] == 0:
                    nowx += 1
                nowy -= 1
                continue
        if nowx > 1:
            if data[nowy][nowx - 1] == 1:
                nowx -= 1
                while data[nowy-1][nowx] == 0:
                    nowx -= 1
                nowy -= 1
                continue
        nowy -= 1
    print(nowx)