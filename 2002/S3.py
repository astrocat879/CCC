r = int(input())
c = int(input())
def finalposition(x, y, direction, steps, grid, dicte):
    for i in steps:
        if i == 'F':
            try:
                x += direction[0]
                y += direction[1]
                if grid[y][x] == 'X' or x < 0 or y < 0:
                    return -1
            except:
                return -1
        elif i == 'L':
            direction = dicte[(direction[0], direction[1])][0]
        elif i == 'R':
            direction = dicte[(direction[0], direction[1])][1]
    return [x, y]
directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
dicte = {(1, 0):[[0,-1], [0,1]], (0, -1):[[-1,0], [1, 0]], (0, 1):[[1, 0], [-1, 0]], (-1, 0):[[0,1], [0,-1]]}
grid = []
points = []
for i in range(r):
    line = list(input())
    grid.append(line)
    for idx, char in enumerate(line):
        if char == '.':
            points.append([idx, i])
m = int(input())
steps = []
for i in range(m):
    step = input()
    steps.append(step)

for i in points:

    for direction in directions:

        a = finalposition(i[0], i[1], direction, steps, grid, dicte)
        if a != -1:
            grid[a[1]][a[0]] = '*'

for i in grid:
    print(''.join(i))
