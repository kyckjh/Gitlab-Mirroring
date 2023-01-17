infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
sum_age = 0
for info_dict in infos:
    sum_age += info_dict.get('age')
print(sum_age)