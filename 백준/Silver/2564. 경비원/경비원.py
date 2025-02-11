import sys
input = sys.stdin.readline

x,y = map(int,input().split())

shop = int(input())
location = []
for _ in range(shop):
    side, pos = map(int,input().split())
    location.append([side,pos])

now_side, now_pos = map(int,input().split())
answer = 0
for side,pos in location:
    if now_side == 1:
        if side == 1:
            answer+= abs(pos-now_pos) 
        elif side == 2:
            answer+= min(now_pos+y+pos,x-now_pos+y+x-pos)
        elif side == 3:
            answer+= pos + now_pos
        elif side == 4:
            answer+= x-now_pos + pos
    elif now_side == 2:
        if side == 1:
            answer+= min(now_pos+y+pos,x-now_pos+y+x-pos)
        elif side == 2:
            answer+= abs(pos-now_pos)
        elif side == 3:
            answer+= now_pos+(y-pos)
        elif side == 4:
            answer+= (x-now_pos) + (y-pos)
    elif now_side == 3:
        if side == 1:
            answer+= pos + now_pos
        elif side == 2:
            answer+= y-pos + now_pos
        elif side == 3:
            answer+= abs(pos-now_pos)
        elif side == 4:
            answer+= min(now_pos+x+pos,y-pos+x+y-now_pos)
    elif now_side == 4:
        if side == 1:
            answer+= now_pos + x-pos
        elif side == 2:
            answer+= y-now_pos + x-pos
        elif side == 3:
            answer+= min(now_pos+x+pos,y-pos+x+y-now_pos)
        elif side == 4:
            answer+= abs(pos-now_pos)
print(answer)
