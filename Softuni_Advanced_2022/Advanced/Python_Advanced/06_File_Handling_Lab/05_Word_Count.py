words_dict = {}

with open('./resources/words.txt', 'r') as words_file:
    all_words = words_file.read().split()
    words_dict = {word.lower(): 0 for word in all_words}

with open('./resources/input.txt', 'r') as text_file:
    for line in text_file:
        for word in words_dict:
            count = line.lower().count(word)
            words_dict[word] += count


print(words_dict)