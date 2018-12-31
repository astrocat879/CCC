import sys
import math
def nearestSquare(number):
    root = math.sqrt(number)
    root = int(root)
    return root
def vertical(direction, x, y):
    if direction == 'd':
        y += 1
    elif direction == 'u':
        y -= 1

    return y
def horizontal(direction, x , y):
    if direction == 'l':
        x -= 1
    if direction == 'r':
        x += 1
    return x
start = int(sys.stdin.readline())
end = int(sys.stdin.readline())
if start == end:
    print(str(start))
else:
    current = start
    x = nearestSquare(end-start+1)
    y = nearestSquare(end-start+1)
    spiral = []
    difference = end-start+1 - (x ** 2)
    if difference >= 1:
        y += 1
    if difference >= x:
        x += 1
    for i in range(y):
        spiral.append([])
    for i in spiral:
        for a in range(x):
            i.append(' ')

    x = math.ceil(x/2) - 1
    y = math.ceil(y/2) - 1
    direction = 'd'

    while current <= end:
        spiral[y][x] = current
        if direction == 'd':
            y = vertical(direction, x, y)
            if spiral[y][x+1] == ' ':
                direction = 'r'
        elif direction == 'r':
            x = horizontal(direction, x, y)
            if spiral[y-1][x] == ' ':
                direction = 'u'
        elif direction == 'u':
            y = vertical(direction, x, y)
            if spiral[y][x-1] == ' ':
                direction = 'l'
        elif direction == 'l':
            x = horizontal(direction, x, y)
            if spiral[y+1][x] == ' ':
                direction = 'd'
        current += 1

    for i in spiral:
        a = ''
        for b in i:

            if len(str(b)) == 1:
                a += ' ' + ' ' + str(b)
            else:
                a += ' ' + str(b)
        print(a)
