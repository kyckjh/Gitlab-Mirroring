# 리스트를 인자로 받아서 복사하여 리스트를 반환하는 함수
def my_deep_copy(target):
    target_copy = []    
    for e in target:
        if type(e) == int or type(e) == str: 
            target_copy.append(e)
        elif type(e) == list:
            copied_list = my_deep_copy(e)
            target_copy.append(copied_list)
    return target_copy

a =[1,2,[3,[4, 5]]]
b = my_deep_copy(a)
b[2][1][0] = 0
print(a, b)