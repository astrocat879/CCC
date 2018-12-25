cards = input()

newdict = {"C":[[],0], "D":[[], 0], "H" : [[], 0], "S" : [[], 0]}
bool = False
totalpoints = 0
current = None
for i in cards:
    if i in newdict:
        current = i
        bool = True
    elif bool:
        newdict[current][0].append(i)
for value in newdict.values():
    if value[0] == []:
        value[1] += 3
        totalpoints += 3
    elif len(value[0]) == 1:
        value[1] += 2
        totalpoints += 2
    elif len(value[0]) == 2:
        value[1] += 1
        totalpoints += 1
    for card in value[0]:
        if card == "A":
            totalpoints += 4
            value[1] += 4
        elif card == "K":
            totalpoints += 3
            value[1] += 3
        elif card == "Q":
            totalpoints += 2
            value[1] += 2
        elif card == "J":
            totalpoints += 1
            value[1] += 1
        else:
            pass

print("Cards Dealt              Points")
print("Clubs " + " ".join(newdict["C"][0]) + "             " + str(newdict["C"][1]))
print("Diamonds " + " ".join(newdict["D"][0]) + "             " + str(newdict["D"][1]))
print("Hearts " + " ".join(newdict["H"][0]) + "             " + str(newdict["H"][1]))
print("Spades " + " ".join(newdict["S"][0]) + "             " + str(newdict["S"][1]))
print("                          Total " + str(totalpoints))
#Looks weird, works on dmoj
