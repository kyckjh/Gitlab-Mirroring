class Link:
    def __init__(self, char):
        self.next = None
        self.prev = None
        self.char = char

T = int(input())
for t in range(1, T+1):
    word = input()
    first = Link(word[0])
    last = Link(word[1])
    first.next = last
    last.prev = first
    for i in range(2, len(word)):
        temp = Link(word[i])
        last.next = temp
        temp.prev = last
        last = temp

    while first.next != None:
        if first.char == first.next.char:
            if first.prev != None:
                first = first.prev
                next = first.next.next.next # 두칸 건너뛰기
                first.next = next
                if next != None:
                    next.prev = first
            else:
                first = first.next.next
                first.prev = None
        else:
            first = first.next
    result = 1
    while first.prev != None:
        result += 1
        first = first.prev

    print(f'#{t} {result}')