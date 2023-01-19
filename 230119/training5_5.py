words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

result = []
for word in words_dict.keys():
    # 첫번째 글자가 b, m, p 중에 하나면 true 
    if len(list(filter(lambda char : char == word[0], ['b', 'm', 'p']))):
        result.append(f'im{word}')
    elif word[0] == 'l':
        result.append(f'il{word}')
    elif word[0] == 'r':
        result.append(f'ir{word}')
    else:
        result.append(f'in{word}')
        
result.sort()
for word in result:
    print(word)