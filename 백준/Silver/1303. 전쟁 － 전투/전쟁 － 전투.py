import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split())

graph = []
visited = [[0]*n for _ in range(m)]

for _ in range(m):
    temp = input().strip()
    graph.append(temp)

def dfs(color,x,y):
    global cnt_w,cnt_b
    if x<0 or x>=n or y<0 or y>=m:
        return
    if visited[y][x] == 1:
        return

    if graph[y][x] != color:
        return

    visited[y][x] = 1
    if color == 'W':
        cnt_w += 1
    else:
        cnt_b += 1
    dfs(color,x+1,y)
    dfs(color,x-1,y)
    dfs(color,x,y+1)
    dfs(color,x,y-1)

cnt_w = 0
cnt_b = 0
sum_w = 0
sum_b = 0

for y in range(m):
    for x in range(n):
        if visited[y][x] == 0 :
            color = graph[y][x]
            dfs(color,x,y)
            if color == 'W':
                sum_w += cnt_w ** 2
                cnt_w = 0
            else:
                sum_b += cnt_b ** 2
                cnt_b = 0
print(sum_w, sum_b)
