n = int(input())
m = int(input())
ads = []
nouns = []
for i in range(n):
    ad = input()
    ads.append(ad)
for i in range(m):
    noun = input()
    nouns.append(noun)
for ad in ads:
    for noun in nouns:
        print(ad, noun, sep=" as ")
