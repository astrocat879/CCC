a = int(input())
b = int(input())

def gcf(a, b):
  n = min([a, b])
  for i in range(n, 0, -1):
    if (a%i == 0) and (b%i == 0):
      return i
  else:
    return 1
if a == 0:
  print(0)

elif a == b:
  print(1)
else:
  mixednumber = a//b
  
  if mixednumber != 0:
    numerator = a - mixednumber * b
    gcfe = gcf(numerator, b)
    if numerator == 0:
      print(mixednumber)
    else:
      print(str(mixednumber) + " " + str(numerator//gcfe) + "/" + str(b//gcfe))
  else:
    gcfe = gcf(a, b)

    print(str(a//gcfe) + "/" + str(b//gcfe))
