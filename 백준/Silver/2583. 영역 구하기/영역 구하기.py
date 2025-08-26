import sys
sys.setrecursionlimit(100000)


m, n, k = map(int,input().split())

graph = [[1] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]

for _ in range(k):
    a,b,c,d = map(int,input().split())

    for i in range(a,c):
        for j in range(b,d):
            graph[j][i] = 0
    
def dfs(graph, visited, x,y,m,n):
    global area
    if x<0 or y<0 or x>=n or y>=m:
        return
    if graph[y][x] == 0:
        return
    if visited[y][x] == 1:
        return

    visited[y][x] = 1
    area += 1

    dfs(graph, visited, x+1,y,m,n)
    dfs(graph, visited, x-1,y,m,n)
    dfs(graph, visited, x,y+1,m,n)
    dfs(graph, visited, x,y-1,m,n)
    
cnt = 0
area = 0
area_arr = []
for y in range(m):
    for x in range(n):
        if graph[y][x] == 1 and visited[y][x] == 0:
            dfs(graph, visited, x,y,m,n)
            cnt +=1
            area_arr.append(area)
            area = 0

area_arr.sort()
print(cnt)
for ar in area_arr:
    print(ar, end=' ')
