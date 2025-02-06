from collections import deque

TC = int(input())

for _ in range(TC):
    n,m = map(int,input().split())
    rank = deque(map(int,input().split()))
    Q=deque()
    for i in range(1,n+1):
        Q.append(i)
    
    num = Q[m]
    arr=[]
    while rank:
        k = max(rank)
        a = rank.popleft()
        b = Q.popleft()
        if k == a:
            arr.append(b)
        elif k !=a:
            rank.append(a)
            Q.append(b)
    print(arr.index(num)+1)