arr = [7,8,9,9,9,9]
count = [0] * 10
for i in range(len(arr)):
    count[arr[i]] += 1

run_cnt = 0
tri_cnt = 0

i = 0
while i < len(count) - 2:
    if count[i] >= 3:
        tri_cnt += 1
        count[i] -= 3
        i -= 1
    elif count[i] * count[i+1] * count[i+2] != 0:
        run_cnt += 1
        count[i] -= 1
        count[i+1] -= 1
        count[i+2] -= 1
        i -= 1
    i += 1
if run_cnt + tri_cnt == 2:
    print('baby gin!')
else:
    print('not baby gin')

    
print(3 and 5)  # True and True -> 3
print(0 and 5)  # False and (True) -> 0
print(5 and 0)  # True and False -> 0
print(3 or 5)   # True and (True) -> 3
print(0 or 3)   # False and True -> 3
print(3 or 0)   # True and (False) -> 3
