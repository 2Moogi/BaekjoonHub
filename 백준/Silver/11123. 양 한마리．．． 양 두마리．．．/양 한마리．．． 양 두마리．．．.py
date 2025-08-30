import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

TC = int(input())

graph = []

def dfs(x,y):
    global cnt
    if x<0 or y<0 or x>=m or y>=n:
        return
    if visited[y][x] == 1:
        return
    if graph[y][x] == '.':
        return

    visited[y][x] = 1

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

for _ in range(TC):
    n,m = map(int,input().split())
    graph = []
    visited = [[0]*m for _ in range(n)]

    for _ in range(n):
        temp = input().strip()
        graph.append(list(temp))

    cnt = 0
    
    for y in range(n):
        for x in range(m):
            if graph[y][x] == '#' and visited[y][x] == 0:
                dfs(x,y)
                cnt+=1
    print(cnt)
