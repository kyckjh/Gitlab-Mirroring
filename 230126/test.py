sample_list = [11, 22, 33, 55, 66]

# 주어진 리스트의 3번 인덱스에 있는 항목을 제거하고 변수에 할당

a = sample_list.pop(3)

print(a, sample_list)

sample_list.append(77)

print(sample_list)

sample_list.insert(2, a)

print(sample_list)