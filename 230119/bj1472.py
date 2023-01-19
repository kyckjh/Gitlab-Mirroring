lst = list(map(int, input()))
lst.sort()
result = 0
ten = 1
for i in range(len(lst)):
    result += lst[i] * ten
    ten *= 10
    
print(result)

