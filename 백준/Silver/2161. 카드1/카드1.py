from collections import deque

n=int(input())

q=deque()

for i in range(1,n+1):
    q.append(i)

if n==1:
    print(1)
else:
    while True:
        print(q.popleft(),end=' ')
        b=q.popleft()
        q.append(b)
        if len(q)==1:
            print(q[0])
            break
    
