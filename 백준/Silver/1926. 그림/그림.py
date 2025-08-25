import sys
sys.setrecursionlimit(1000000000)


n, m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    arr = list(map(int,input().split()))
    graph.append(arr)
        
def dfs(graph, visited, x,y,n,m):
    global count
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if graph[y][x] == 0:
        return
    if visited[y][x] == 1:
        return

    visited[y][x] = 1
    count += 1

    dfs(graph, visited, x+1,y,n,m)
    dfs(graph, visited, x-1,y,n,m)
    dfs(graph, visited, x,y+1,n,m)
    dfs(graph, visited, x,y-1,n,m)
    
cnt = 0
grim = []
count = 0
for y in range(n):
    for x in range(m):
        if visited[y][x] == 0 and graph[y][x] == 1:
            dfs(graph, visited, x,y,n,m)
            cnt += 1
            grim.append(count)
            count = 0

if cnt == 0:
    size = 0
else:
    size = max(grim)
print(cnt)
print(size)

