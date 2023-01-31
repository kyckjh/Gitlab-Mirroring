class Stack:
    def __init__(self):
        self.stack_lst = []
    def empty(self):
        if len(self.stack_lst):
            return False
        else:   # len이 0이면 False가 되므로 empty()는 True
            return True
    def top(self):
        try:    # 스택의 마지막 원소 반환
            return self.stack_lst[-1]
        except IndexError:  # 마지막 원소가 없으면 None 반환
            return None
    def pop(self):
        if self.empty():  # 스택이 비었으면 None 반환
            return
        else:   # 스택에 원소가 있으면 마지막 원소 제거 후 반환
            return self.stack_lst.pop(-1)
    def push(self, value):  # 리스트의 마지막에 값 추가
        self.stack_lst.append(value)    
    def __repr__(self):
        st = ' '
        if self.empty():    # 스택이 비었으면 'None' 반환
            return 'None'
        return st.join(str(x) for x in self.stack_lst)  # 리스트의 값 str 형식으로 반환

ss = Stack()
ss.push(3)
print(ss)

ss.push(4)
ss.push(5)
ss.push(6)
print(ss)
print(ss.top())
print(ss)
ss.pop()
print(ss)
ss.push(79)
print(ss)
ss.pop()
ss.pop()
ss.pop()
ss.pop()
print(ss)
print(ss.top())
print(ss.pop())