import sys

daynumber = int(sys.stdin.readline())
monthdays = int(sys.stdin.readline())
print("Sun Mon Tue Wed Thr Fri Sat")
month = []
week = []
for i in range(1, (monthdays+1)):

    if (len(week) == 7) or (i == monthdays):
        if i == monthdays:
            if len(str(i)) == 2:
                week.append(" " + str(i))
            else:
                week.append("  " + str(i))
        month.append(week)
        week = []
    if i == 1:
        for d in range(daynumber - 1):
            week.append("   ")
        if len(str(i)) == 2:
            week.append(" " + str(i))
        else:
            week.append("  " + str(i))
    else:
        if len(str(i)) == 2:
            week.append(" " + str(i))
        else:
            week.append("  " + str(i))

for week in month:
  if monthdays in week:
      print(" ".join(week) + "\n")
  else:
    print(" ".join(week))
