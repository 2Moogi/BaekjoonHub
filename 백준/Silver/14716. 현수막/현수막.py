import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

m, n = map(int,input().split())
graph = []
visited = [[0]*n for _ in range(m)]

for _ in range(m):
    temp = list(map(int,input().split()))
    graph.append(temp)

def dfs(x,y):
    global cnt
    if x<0 or y<0 or x>=n or y>=m:
        return
    if graph[y][x] == 0:
        return
    if visited[y][x] == 1:
        return

    visited[y][x] = 1

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    
    dfs(x+1,y+1)
    dfs(x+1,y-1)
    dfs(x-1,y+1)
    dfs(x-1,y-1)

cnt = 0

for y in range(m):
    for x in range(n):
        if graph[y][x] == 1 and visited[y][x] == 0:
            dfs(x,y)
            cnt+=1
print(cnt)
    
