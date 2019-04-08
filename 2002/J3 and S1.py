
pi = int(input())
gr = int(input())
re = int(input())
ora = int(input())
money = int(input())
mins = []
for p in range(money//pi+1):
    for g in range(money // gr + 1):
        for r in range(money // re + 1):
            for o in range(money // ora + 1):
                if (p * pi) + (g * gr) + (r * re) + (o * ora) == money:
                    print("# of PINK is {} # of GREEN is {} # of RED is {} # of ORANGE is {}".format(p, g, r, o))
                    mins.append(p+g+r+o)
print("Total combinations is {}.".format(str(len(mins))))
print("Minimum number of tickets to print is {}.".format(str(min(mins))))
