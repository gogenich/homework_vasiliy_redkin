words = input('введите слова через пробел: ')
words = words.split()
i = 1
for word in words:
    print(f'{i} {word[: 10]}')
    i = i + 1
