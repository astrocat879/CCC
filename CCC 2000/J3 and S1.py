import sys
quarters = int(sys.stdin.readline()) #rip pennies
firstmachine = int(sys.stdin.readline())
secondmachine = int(sys.stdin.readline())
thirdmachine = int(sys.stdin.readline())
def check(quarters):
    if quarters == 0:
        return True
counter = 0
while True:
  if quarters == 0:
      break
  quarters -= 1
  firstmachine += 1
  counter += 1
  if firstmachine == 35:
    quarters += 30
    firstmachine = 0
  if quarters == 0:
      break
  quarters -= 1
  secondmachine += 1
  counter += 1
  if secondmachine == 100:
    quarters += 60
    secondmachine = 0
  if quarters == 0:
      break
  quarters -= 1
  thirdmachine += 1
  counter += 1
  if thirdmachine == 10:
    quarters += 9
    thirdmachine = 0

print("Martha plays " + str(counter) + " times before going broke.")
