words = ["eat", "tea", "tan", "ate", "nat", "bat"]

sorted_words = map(sorted, words)

words_dict = {key : [] for key in set(map(tuple, sorted_words))}

for word in words:
    sorted_word = tuple(sorted(word))
    words_dict[sorted_word].append(word)

print(words_dict.values())