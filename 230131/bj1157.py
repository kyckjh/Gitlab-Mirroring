s = input().upper()
s_dict = dict()
for char in s:
    s_dict.setdefault(char, 0)
    s_dict[char] += 1
a = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)

if len(a) > 1 and a[0][1] == a[1][1]:
    print('?')
else:
    print(a[0][0])