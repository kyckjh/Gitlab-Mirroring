import sys
sys.stdin = open("input.txt", "r")

class Node:
    def __init__(self, value, left = 0, right = 0):
        self.left = int(left)
        self.right = int(right)
        self.value = value

def postorder(idx):
    node = values[idx]
    if node.left == 0:
        return int(node.value)
    if node.value == '+':
        return postorder(node.left) + postorder(node.right)
    if node.value == '-':
        return postorder(node.left) - postorder(node.right)
    if node.value == '/':
        return postorder(node.left) // postorder(node.right)
    return postorder(node.left) * postorder(node.right)

for t in range(1,11):
    N = int(input())
    values = [0]
    for _ in range(N):
        data = input().split()
        values.append(Node(*data[1:]))
    print(f'#{t} {postorder(1)}')

