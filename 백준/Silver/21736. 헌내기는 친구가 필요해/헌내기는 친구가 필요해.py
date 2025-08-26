import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
def dfs(graph, visited, x,y,n,m):
    global cnt
    if x<0 or y<0 or x>=m or y>=n:
        return
    if visited[y][x] == 1:
        return
    if graph[y][x] == 'X':
        return

    visited[y][x] = 1
    
    if graph[y][x] == 'P':
        cnt += 1
        
    dfs(graph, visited, x+1,y,n,m)
    dfs(graph, visited, x-1,y,n,m)
    dfs(graph, visited, x,y+1,n,m)
    dfs(graph, visited, x,y-1,n,m)

n, m = map(int,input().split())
graph = []
visited = [[0]*m for _ in range(n)]
for _ in range(n):
    temp = input()
    graph.append(temp)
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            dfs(graph, visited, j,i,n,m)
            ynum = i
            xnum = j

if cnt == 0:
    print('TT')
else:
    print(cnt)


