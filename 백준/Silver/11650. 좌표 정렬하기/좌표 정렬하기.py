import sys

input = sys.stdin.readline

TC = int(input())
arr=[]
for _ in range(TC):
    x, y = map(int,input().split())
    arr.append([x,y])
arr.sort()
arr2 = sorted(arr, key=lambda x:y)
for i in range(len(arr)):
    print(arr[i][0], arr[i][1])