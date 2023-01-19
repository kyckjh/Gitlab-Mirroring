N = int(input())
result = 0
for i in range(N):
    word = input()
    lastchar = ''
    length = 0
    for char in word:
        if(lastchar != char):
            length += 1
            lastchar = char
    word_set = set(word)
    if(len(word_set) == length):
        result += 1
print(result)