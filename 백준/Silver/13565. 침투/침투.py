import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

m, n = map(int,input().split())
graph = []
visited = [[0]*n for _ in range(m)]


for _ in range(m):
    temp = input().strip()
    graph.append(list(temp))

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return
    if graph[y][x] == '1':
        return
    if visited[y][x] == 1:
        return

    visited[y][x] = 1

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

for y in range(1):
    for x in range(n):
        if graph[y][x] == '0' and visited[y][x] == 0:
            dfs(x,y)

if sum(visited[-1]) > 0:
    print('YES')
else:
    print('NO')


            

    
