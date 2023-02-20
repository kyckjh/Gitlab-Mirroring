import sys
A, B, C = map(int, sys.stdin.readline().split())
D = int(sys.stdin.readline())
temp = D // 3600
A += temp
D %= 3600

temp = D // 60
B += temp
D %= 60

temp = D
C += temp

c = C // 60
C %= 60
B += c

b = B // 60
B %= 60
A += b

A %= 24
print(A, B, C)