user_words = input('input random gibberish- ')
word_list = user_words.split()
user_words = []

for word in word_list:
    user_words.append(word)
print(user_words)

for ind, el in enumerate(user_words):
    if len(el) < 10:
        print(ind, el)
    else:
        print(ind, el[0:10])
