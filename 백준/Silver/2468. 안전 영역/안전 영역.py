import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    temp = list(map(int,input().split()))
    graph.append(temp)

maxi = 0
for i in range(n):
    for j in range(n):
        maxi = max(graph[i][j] ,maxi)

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return
    if graph[y][x] <= 0:
        return
    if visited[y][x] == 1:
        return

    visited[y][x] = 1
    
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

height_arr = []


for k in range(0,maxi):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            graph[y][x] -= k

    for y in range(n):
        for x in range(n):
            if graph[y][x] > 0 and visited[y][x] == 0:
                dfs(x,y)
                cnt += 1
    height_arr.append(cnt)

    for y in range(n):
        for x in range(n):
            graph[y][x] += k
print(max(height_arr))
                
