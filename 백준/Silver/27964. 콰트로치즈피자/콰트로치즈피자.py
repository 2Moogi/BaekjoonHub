import sys
input = sys.stdin.readline

n = int(input())

clist=list(input().split())
arr=[]
for c in clist:
    if len(c) > 5 and c[-6:] == 'Cheese':
        arr.append(c)
arr =set(arr)
if len(arr) >= 4 :
    print('yummy')
else:
    print('sad')
