from sys import stdin
import heapq
input = stdin.readline
c, r, d = map(int, input().split(" "))
maxweightsneeded = [0]*c
dicte = {}
for i in range(r):
    x, y, w = map(int, input().split(" "))
    if x not in dicte:
        dicte[x] = []
    if y not in dicte:
        dicte[y] = []
    dicte[x].append([y, w])
    dicte[y].append([x, w])
queue = [[1, 99999]]
heapq.heapify(queue)
while queue:
    city, weight = heapq.heappop(queue)
    for nc, nw in dicte[city]:
        if weight <= nw:
            if weight > maxweightsneeded[nc - 1]:
                maxweightsneeded[nc - 1] = weight
                heapq.heappush(queue,[nc, weight])
        else:
            if nw > maxweightsneeded[nc - 1]:
                maxweightsneeded[nc - 1] = nw
                heapq.heappush(queue, [nc, weight])
values = 99999
for i in range(d):
    destination = int(input())
    newdestination = maxweightsneeded[destination-1]
    if newdestination < values:
        values = newdestination
print(values)
