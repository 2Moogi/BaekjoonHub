import sys
input=sys.stdin.readline
n=int(input())

arr1 = list(map(int,input().split()))
dict={}
for num in arr1:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
        
m = int(input())
arr2 = list(map(int,input().split()))


for num in arr2:
    if num in dict:
        print(dict[num], end=' ')
    else:
        print(0, end=' ')
