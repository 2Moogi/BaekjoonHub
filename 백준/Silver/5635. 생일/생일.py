import sys

input = sys.stdin.readline

n = int(input())
arr=[]
for _ in range(n):
    name,d,m,y = input().split()
    arr.append([name,d,m,y])
arr.sort(key=lambda x:int(x[1]))
arr.sort(key=lambda x:int(x[2]))
arr.sort(key=lambda x:int(x[3]))
print(arr[-1][0])
print(arr[0][0])