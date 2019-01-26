while True:
    word = input()
    if word == 'quit!':
        break
    if len(word) > 4:
        if word[-2:] == 'or' and (word[-3] not in 'aeiuo'):
            word = list(word)
            word.insert(-1, 'u')


    print(''.join(word))
