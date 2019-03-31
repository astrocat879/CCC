import math
memory = {}
def isprime(number):
    if number in memory:
        return memory[number]
    if number % 10 in [2,4,6,8,5,0] and number not in [5, 1, 2]:
        memory[number] = False
        return False
    else:
        for i in range(2,int(math.sqrt(number)) + 1):
            if number % i == 0:
                memory[number]= False
                return False
        memory[number] = True
        return True
T = int(input())
for num in range(T):
    line = int(input())
    for i in range(2, line):
        a = 2 * line - i
        b = i
        if isprime(a) and isprime(b):
            print(str(a) + " " + str(b))
            break
