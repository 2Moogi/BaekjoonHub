import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

graph = []
visited = [[0]*n for _ in range(n)]

for _ in range(n):
    temp = input().strip()
    graph.append(list(temp))
graph2 = list(graph)

def dfs(color,x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return
    if visited[y][x] == 1:
        return

    if graph[y][x] != color:
        return

    visited[y][x] = 1
    
    dfs(color,x+1,y)
    dfs(color,x-1,y)
    dfs(color,x,y+1)
    dfs(color,x,y-1)

cnt_normal = 0
cnt_blind = 0

for y in range(n):
    for x in range(n):
        if visited[y][x] == 0 :
            color = graph[y][x]
            dfs(color,x,y)
            cnt_normal+=1
            
for y in range(n):
    for x in range(n):
        if graph[y][x] == 'R':
            graph[y][x] = 'G'
            
visited = [[0]*n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if visited[y][x] == 0 :
            color = graph[y][x]
            dfs(color,x,y)
            cnt_blind+=1
print(cnt_normal, cnt_blind)
