class Chars:
    def __init__(self, char):
        self.char = char
        self.pre = None
        self.next = None

    def connect_pre(self, other):
        self.pre = other
        other.next = self

    def connect_next(self, other):
        self.next = other
        other.pre = self


import sys
inputs = sys.stdin.readline()
first = Chars('!')
cursor = Chars(inputs[0])
cursor.connect_pre(first)
for i in range(1, len(inputs)-1):
    temp = Chars(inputs[i])
    temp.connect_pre(cursor)
    cursor = temp
N = int(sys.stdin.readline())
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'L':
        if cursor.pre != None:
            cursor = cursor.pre
    elif order[0] == 'D':
        if cursor.next != None:
            cursor = cursor.next
    elif order[0] == 'B':
        if cursor == first:
            continue
        elif cursor.next == None:
            cursor = cursor.pre
            cursor.next = None
        else: # cursor.next가 None이 아니면, cursor을 한 칸 앞으로 옮기고 한칸 건너뛰고 연결
            cursor = cursor.pre
            cursor.connect_next(cursor.next.next)
    else: # 단어 추가하고 커서 오른쪽으로 한칸 가기
        new = Chars(order[1])
        if cursor.next == None:
            cursor.connect_next(new)
        else:
            new.connect_next(cursor.next)
            cursor.connect_next(new)
        cursor = cursor.next


while first.next != None:
    first = first.next
    print(first.char, end='')