import sys
x = int(sys.stdin.readline())
m = int(sys.stdin.readline())
a = False
for n in range(1,m):
    a = (x*n) % m
    if a == 1:
        print(str(n))
        a = True
        break


if not(a):
    print('No such integer exists.')


