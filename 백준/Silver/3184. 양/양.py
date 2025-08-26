import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int,input().split())

graph = []
visited = [[0]*m for _ in range(n)]

answer_lamb = 0
answer_wolf = 0

for _ in range(n):
    temp = input()
    graph.append(temp)

def dfs(graph, visited, x,y,n,m):
    global lamb_cnt
    global wolf_cnt
    if x<0 or y<0 or x>=m or y>=n:
        return
    if visited[y][x] == 1:
        return
    if graph[y][x] == '#':
        return

    visited[y][x] = 1

    if graph[y][x] == 'o':
        lamb_cnt += 1
    if graph[y][x] == 'v':
        wolf_cnt += 1

    dfs(graph, visited, x+1,y,n,m)
    dfs(graph, visited, x-1,y,n,m)
    dfs(graph, visited, x,y+1,n,m)
    dfs(graph, visited, x,y-1,n,m)

lamb_cnt = 0
wolf_cnt = 0
    
for y in range(n):
    for x in range(m):
        if graph[y][x] != '#' :
            if visited[y][x] == 0:
                dfs(graph,visited ,x,y,n,m)
                if lamb_cnt > wolf_cnt :
                    answer_lamb += lamb_cnt
                else:
                    answer_wolf += wolf_cnt
                wolf_cnt = 0
                lamb_cnt = 0
print(answer_lamb, answer_wolf)




            
