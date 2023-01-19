N = int(input())
len_dict = {}
for i in range(N):
    word = input()
    len_dict.setdefault(len(word), [])
    len_dict[len(word)].append(word)
    
for value in len_dict.values():
    value.sort()
result = []
while(len(len_dict) > 0):
    min_num = min(len_dict.keys())
    for num in len_dict[min_num]:
        result.append(num)
    len_dict.pop(min_num)

lastword = ''
for word in result:
    if(lastword != word):
        print(word)
        lastword = word