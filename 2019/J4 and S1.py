line = input()
line = list(line)
top = ['1', '2']
bottom = ['3', '4']
for i in line:
    if i == 'H':
        top, bottom = bottom, top
    elif i == 'V':
        top = top[::-1]
        bottom = bottom[::-1]
print(" ".join(top))
print(" ".join(bottom))
