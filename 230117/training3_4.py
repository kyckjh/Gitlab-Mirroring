blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_dict = {'A' : 0, 'B' : 0, 'AB' : 0, 'O' : 0}

for type in blood_types:
    blood_dict[type] += 1
    
print(blood_dict)