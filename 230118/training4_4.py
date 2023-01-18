word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

sum1 = 0
sum2 = 0
for word in word1:
    sum1 += ord(word)
for word in word2:
    sum2 += ord(word)
    
if sum1 > sum2:
    print(word1)
else:
    print(word2)