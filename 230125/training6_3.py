def count_vowels(word):
    cnt = sum([word.count(a) for a in ['a', 'e', 'i', 'o', 'u']])
    print(cnt)

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3
