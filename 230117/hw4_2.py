words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

lastword = words[0][0]
index = 1
for word in words:
    if word[0] != lastword:
        print(f'{index}번째 사람이 탈락했습니다.')
    else:
        print(word)
        lastword = word[-1]
    index += 1
        
input_word = input()
while(input_word != 'done'):
    if(input_word[0] != lastword):
        print(f'{index}번째 사람이 탈락했습니다.')
        break
    else:
        lastword = input_word[-1]
    input_word = input()
    index += 1
print('끝말잇기가 종료되었습니다.')