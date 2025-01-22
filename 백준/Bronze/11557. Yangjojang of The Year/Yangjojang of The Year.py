import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    n=int(input())
    arr=[]
    for _ in range(n):
        univ, L = input().split()
        arr.append([univ,L])
    arr.sort(key = lambda x:int(x[1]))
    print(arr[-1][0])