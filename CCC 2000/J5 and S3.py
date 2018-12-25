import sys

class Site:
    def __init__(self, url):
        self.url = url
        self.neighbours = []
    def __repr__(self):
      return "url: {}, neighbours: {}".format(self.url, str([n.url for n in self.neighbours]))
siteno = int(sys.stdin.readline())
site_map = {}

for n in range(siteno):
  sitename = input()
  current = None
  if sitename not in site_map:
    current = Site(sitename)
    site_map[sitename] = current
  else:
    current = site_map[sitename]

  line = input()
  while line != "</HTML>":
    linelist = line.split('"')
    for idx, i in enumerate(linelist):
      if "HREF" in i:
        url = linelist[idx+1]
        neighbour = None
        if url not in site_map:
          neighbour = Site(url)
          site_map[url] = neighbour
        else:
          neighbour = site_map[url]

        if neighbour not in current.neighbours:
          current.neighbours.append(neighbour)
          print("Link from {} to {}".format(sitename, url))
    line = input()

def bfs(start, url):
  visited = []
  queue = []
  queue.append(start)
  while len(queue) > 0:
    current = queue.pop(0)
    if current.url == url:
      return True
    visited.append(current)
    for i in current.neighbours:
      if i not in visited:
        queue.append(i)
  return False


urla = None

while urla != "The End":
    urla = input()
    if urla == "The End":
        break
    urlb = input()
    if urla not in site_map or not bfs(site_map[urla], urlb):
        print("Can't surf from {} to {}.".format(urla, urlb))
    else:
        print("Can surf from {} to {}.".format(urla, urlb))
