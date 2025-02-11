import sys

input = sys.stdin.readline

n = int(input())
sizes = list(map(int,input().split()))
t,p = map(int,input().split())

tcnt=0
for size in sizes:
    if size == 0:
        continue
    else:
        if size % t == 0:
            tcnt += size//t
        else:
            tcnt += size//t +1
print(tcnt)
print(n//p,n%p)