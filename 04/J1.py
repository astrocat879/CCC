import math
number = int(input())
def nearestSquare(number):
    return int(math.sqrt(number))
print("The largest square has side length {}.".format(str(nearestSquare(number))))
