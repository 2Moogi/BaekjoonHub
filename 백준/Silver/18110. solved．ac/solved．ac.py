import math
import sys
input = sys.stdin.readline

n = int(input())
arr=[]
for _ in range(n):
    rank = int(input())
    arr.append(rank)
arr.sort()

cnt = math.floor((n * 0.15)+0.5)

out=[]
for i in range(cnt):
    out.append(arr[i])
for i in range(-1,-cnt-1,-1):
    out.append(arr[i])
    
if n==0:
    print(0)
else:
    v = (sum(arr)-sum(out))/(len(arr)-(cnt*2))
    k = math.floor(v+0.5)
    print(k)