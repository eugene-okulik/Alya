text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, \
    dignissim vitae libero'

words = text.split()
# print(words)
fin_words = []
for word in words:
    if word.endswith(','):
        word = word.replace(',', 'ing,')
        fin_words.append(word)
    elif word.endswith('.'):
        word = word.replace('.', 'ing.')
        fin_words.append(word)
    else:
        word = word + 'ing'
        fin_words.append(word)
print(' '.join(fin_words))
