words = ["eat", "tea", "tan", "ate", "nat", "bat"]

words_dict = {}

for word in words:
    sorted_word = tuple(sorted(word))
    words_dict.setdefault(sorted_word, [])
    words_dict[sorted_word].append(word)
    
print(words_dict.values())