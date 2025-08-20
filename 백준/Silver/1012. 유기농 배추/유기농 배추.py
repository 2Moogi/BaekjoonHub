import sys
sys.setrecursionlimit(1000000)

def dfs(graph, visited, x,y,m,n):
    if x<0 or x>=m or y<0 or y>=n:
        return
    if visited[y][x] == True:
        return
    if graph[y][x] == 0:
        return
    
    visited[y][x] = True

    dfs(graph, visited, x+1,y,m,n)
    dfs(graph, visited, x-1,y,m,n)
    dfs(graph, visited, x,y+1,m,n)
    dfs(graph, visited, x,y-1,m,n)


TC = int(input())

for _ in range(TC):
    m, n, k = map(int,input().split())

    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1
    
    cnt = 0

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and visited[y][x] == False:
                dfs(graph,visited,x,y,m,n)
                cnt += 1
    print(cnt)
    
