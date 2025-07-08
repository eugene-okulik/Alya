text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = text.split()
# print(words)
for word in words:
    if word.endswith(','):
        word = word.replace(',', 'ing,')
        print(word)
    elif word.endswith('.'):
        word = word.replace('.', 'ing.')
        print(word)
    else:
        print(word + 'ing')
