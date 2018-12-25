import sys
def change(liste, chnge):
  if chnge == "join":
    joiningstream = int(sys.stdin.readline())
    newstream = liste[joiningstream - 1] + liste[joiningstream]
    liste[joiningstream-1] = newstream
    del flows[joiningstream]
    return liste
  if chnge == "split":
    stream = int(sys.stdin.readline())
    percent = int(sys.stdin.readline())

    newstreama = (percent / 100) * flows[(stream - 1)]
    newstreamb = (flows[(stream - 1)]) - newstreama
    flows[stream-1] = newstreama
    flows.insert(stream, newstreamb)
    return liste




a = int(sys.stdin.readline())
flows = []
for i in range(a):
    flow = int(sys.stdin.readline())
    flows.append(flow)
join = False
split = False
splitcounter = 0

while True:
    b = int(sys.stdin.readline())
    if b == 99:
      flows = change(flows,"split")
    elif b == 88:
      flows = change(flows,"join")
    elif b == 77:
        break

print(" ".join([str(int(f)) for f in flows]))
