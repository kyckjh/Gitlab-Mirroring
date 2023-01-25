grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

max_cost = 0
max_idx = 0
for idx, grain in enumerate(grain_lst):
    if grain[1] > max_cost:        
        max_cost = grain[1]
        max_idx = idx
print(grain_lst[max_idx][0])