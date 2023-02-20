import sys
lst = list(map(int, sys.stdin.readline().split()))
if lst.count(9):
    print("F")
else:
    print("S")