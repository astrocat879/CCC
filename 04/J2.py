x = int(input())
y = int(input())
print("All positions change in year {}".format(str(x)))
x += 60
while x <= y:
    print("All positions change in year {}".format(str(x)))
    x += 60
