apples = 0
bananas = 0
for i in range(2):
    a = int(input())
    b = int(input())
    c = int(input())
    if i == 0:
        apples = (a * 3) + (b * 2) + c
    else:
        bananas = (a * 3) + (b * 2) + c
if apples > bananas:
    print('A')
elif apples < bananas:
    print('B')
else:
    print('T')
