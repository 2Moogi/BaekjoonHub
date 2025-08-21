import sys
sys.setrecursionlimit(1000000)

def dfs(graph, visited, x,y,w,h):
    if x<0 or x>=w or y<0 or y>=h:
        return
    if visited[y][x] == 1:
        return
    if graph[y][x] == 0:
        return
    
    visited[y][x] = 1

    dfs(graph, visited, x+1,y,w,h)
    dfs(graph, visited, x-1,y,w,h)
    dfs(graph, visited, x,y+1,w,h)
    dfs(graph, visited, x,y-1,w,h)

    dfs(graph, visited, x+1,y+1,w,h)
    dfs(graph, visited, x-1,y-1,w,h)
    dfs(graph, visited, x+1,y-1,w,h)
    dfs(graph, visited, x-1,y+1,w,h)


while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    else:
        cnt = 0
        graph = []
        visited = [[0] * w for _ in range(h)]
        for i in range(h):
            arr = list(map(int,input().split()))
            graph.append(arr)
        
        for y in range(h):
            for x in range(w):
                if visited[y][x] == 0 and graph[y][x] == 1:
                    dfs(graph, visited,x,y,w,h)
                    cnt+=1
        print(cnt)
