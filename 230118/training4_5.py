test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

cheating_list = []
for name, status in test_status.items():
    if status == 'cheating':
        cheating_list.append(name)
    elif status == 'sleeping':
        test_status[name] = 'solving'

for cheater in cheating_list:
    test_status.pop(cheater)

print(sorted(cheating_list))
print('test_status =', test_status)