fruit_lst = list(input().lower().split(','))
print(fruit_lst)

for idx, fruit in enumerate(fruit_lst):
    if fruit.find('rotten') != -1:
        fruit_lst[idx] = fruit[6:]
print(fruit_lst)