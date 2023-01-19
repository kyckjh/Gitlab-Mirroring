# map_obj = map((lambda n : n * 10), [1, 2, 3])
# rlt = list(map_obj)

# print(rlt)
word = 'abc'
if len(list(filter(lambda char : char == word[0], ['b', 'm', 'p']))):
    print('true')
else:
    print('false')