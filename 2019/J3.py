n = int(input())
for i in range(n):
    line = input()
    newline = ''
    char = ''
    charcounter = 1
    for i in line:
        if char == '':
            char = i
        else:
            if i == char:
                charcounter += 1
            else:
                if newline == '':
                    newline += str(charcounter) + ' ' + char
                else:
                    newline += ' ' + str(charcounter) + ' ' + char
                charcounter = 1
                char = i
    if newline == '':
        newline += str(charcounter) + ' ' + char
    else:
        newline += ' ' + str(charcounter) + ' ' + char
    print(newline)
