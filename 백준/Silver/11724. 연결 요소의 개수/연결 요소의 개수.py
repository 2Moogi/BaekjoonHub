import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


n,m = map(int,input().split())


graph=[[]for i in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u] += [v]
    graph[v] += [u]


visited=[0] *(n+1)

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            visited[nx] = 1
            dfs(nx)
            
cnt = 0


for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
        if sum(visited) == n:
            print(cnt)
            break

