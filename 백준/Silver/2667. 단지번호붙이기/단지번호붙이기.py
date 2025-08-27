import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

graph = []
visited = [[0]*n for _ in range(n)]

for _ in range(n):
    temp = input().strip()
    graph.append(temp)


def dfs(x,y):
    global in_cnt
    if x<0 or y<0 or x>=n or y>=n:
        return
    if graph[y][x] == '0':
        return
    if visited[y][x] == 1:
        return

    visited[y][x] = 1
    in_cnt += 1

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

mass_cnt = 0
in_cnt = 0
mass_arr = []
for y in range(n):
    for x in range(n):
        if graph[y][x] == '1' and visited[y][x] == 0:
            dfs(x,y)
            mass_cnt += 1
            mass_arr.append(in_cnt)

            in_cnt = 0

print(mass_cnt)
mass_arr.sort()
for ar in mass_arr:
    print(ar)
