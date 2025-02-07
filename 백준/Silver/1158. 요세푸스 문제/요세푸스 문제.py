from collections import deque
import sys
input=sys.stdin.readline

n, k = map(int,input().split())

Q = deque()
cnt = 0
for i in range(1,n+1):
    Q.append(i)
arr=[]
per='<'
while Q:
    cnt+=1
    if cnt == k:
        arr.append(Q.popleft())
        cnt = 0
    else:
        Q.append(Q.popleft())
print('<', end='')
for i in range(len(arr)):
    if i == len(arr)-1:
        print(arr[i], end='')
    else:
        print(arr[i], end=', ')
print('>')
