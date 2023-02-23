class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
        self.size += 1

    def __str__(self):
        result = '['
        current = self.head
        while current:
            result += (str(current.value)+', ')
        return result

    def pop(self, idx = -1):
        if idx == 0:
            self.head = self.head.next
        elif idx == -1:
            if self.size == 1:
                self.head = None
            current = self.head
            while current.next:
                current = current.next
            for i in range(self.size - 1):
                current = current.next
            current.next = None
        else:
            current = self.head
            prev = None
            for i in range(idx):
                prev = current
                current = current.next
            prev.next = current




lst = MyLinkedList()