n = int(input())
for case in range(n):
    l = int(input())
    first = list(map(int,input().split(" ")))
    second = list(map(int, input().split(" ")))
    dist = []
    for idx, j in enumerate(second):
        if j in first:
            ifront = idx - first.index(j)
            iback = idx - l - 1 - first[::-1].index(j)
            i = [ifront, iback]
            dist.append(max(i))
    if dist:
        print("The maximum distance is " + str(max(dist)))
    else:
        print("The maximum distance is 0")
