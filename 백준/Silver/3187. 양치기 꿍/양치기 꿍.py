import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

r,c = map(int,input().split())
graph = []
visited = [[0] *c for _ in range(r)]
for _ in range(r):
    temp = input().strip()
    graph.append(temp)

def dfs(x,y):
    global kcnt, vcnt
    if x<0 or y<0 or x>=c or y>=r:
        return
    if visited[y][x] == 1:
        return
    if graph[y][x] == '#':
        return

    visited[y][x] = 1
    if graph[y][x] == 'k':
        kcnt += 1
    if graph[y][x] == 'v':
        vcnt += 1

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

lamb, wolf = 0, 0
kcnt, vcnt = 0, 0

for y in range(r):
    for x in range(c):
        if graph[y][x] != '#' and visited[y][x] == 0:
            dfs(x,y)
            if kcnt > vcnt:
                lamb += kcnt
            else:
                wolf += vcnt
            kcnt, vcnt = 0,0
print(lamb, wolf)
