import sys
input = sys.stdin.readline

n = int(input())
rooms=[]
for _ in range(n):
    room = input().strip()
    rooms.append(room)
garocnt = 0
serocnt = 0
for i in range(n):
    dotcnt = 0
    for j in range(n):
        if rooms[i][j] == '.':
            dotcnt+=1
            if dotcnt > 1 and j==n-1:
                garocnt+=1
        elif rooms[i][j] == 'X':
            if dotcnt > 1:
                garocnt+=1
            dotcnt = 0
        
for i in range(n):
    dotcnt = 0
    for j in range(n):
        if rooms[j][i] == '.':
            dotcnt+=1
            if dotcnt > 1 and j == n-1:
                serocnt+=1
        elif rooms[j][i] == 'X':
            if dotcnt > 1:
                serocnt+=1
            dotcnt=0
print(garocnt,serocnt)