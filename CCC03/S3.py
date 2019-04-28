total = int(input())
r = int(input())
c = int(input())
points = []
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def dora(startx, starty, grid, visited):
    if [startx, starty] not in visited:
        if r > starty >= 0 and c > startx >= 0 and grid[starty][startx] == '.':
            if [startx, starty] in points:
                points.remove([startx, starty])
            visited.append([startx, starty])

            for i in directions:
                newx = startx
                newy = starty
                newx += i[0]
                newy += i[1]
                dora(newx, newy, grid, visited)
rooms = []

grid = []
for i in range(r):
    line = list(input())
    grid.append(line)

    for idx, char in enumerate(line):
        if char == '.':
            points.append([idx, i])
counter = 0
while points:
    curpoints = len(points)
    char = points.pop(0)
    dora(char[0], char[1], grid, [])
    nowpoints = len(points)
    rooms.append(curpoints-nowpoints)
rooms.sort(reverse=True)
counter = 0
for i in rooms:
    if total >= i:
        total -= i
        counter += 1
    else:
        break

if counter == 1:

    print('1 room, ' + str(total) + 'square metre(s) left over')
else:
    print(str(counter) + ' rooms, ' + str(total) + ' square metre(s) left over')
