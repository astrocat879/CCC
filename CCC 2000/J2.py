import sys

lowerbound = int(sys.stdin.readline())
upperbound = int(sys.stdin.readline())
counter = 0
for i in range(lowerbound,(upperbound+1)):
    if ('2' in str(i)) or ('3' in str(i)) or ('4' in str(i)) or ('5' in str(i)) or ('7' in str(i)):
      pass
    else:
      a = ''
      for d in reversed(str(i)):
        
        if d == '9':
          a += '6'
        elif d == '6':
          a += '9'
        elif d == '1' or d == '0' or d == '8':
          a += d
        else:
          break

      if a == str(i):
        counter += 1
      
print(counter)
#islayernerds
