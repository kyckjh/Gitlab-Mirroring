num_str = input()
last_str = num_str[0]
change = 0
for char in num_str:
    if char != last_str:
        last_str = char
        change += 1
if change == 1:
    print(1)
else:
    print(change // 2 + change % 2)