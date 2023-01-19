def sum_of_repeat_number(num_list):
    sum1 = sum(num_list)
    num_set = set(num_list)
    for n in num_set:
        num_list.remove(n)
    sum2 = sum(num_list)
    sum3 = sum(set(num_list))
    return sum1 - sum2 - sum3

num_list = [4, 4, 7, 8, 10, 4]
print(sum_of_repeat_number(num_list))

# 출력 예시 
#  25

