start = 1
slad = {40:64, 54:19, 9:34, 90:48,67:86, 99:77}
while True:
    move = int(input())
    if move == 0:
        print("You Quit!")
        break
    if start + move <= 100:
        start += move
    if start in slad:
        start = slad[start]
    print("You are now on square", str(start), sep= " ")
    if start == 100:
        print("You Win!")
        break
