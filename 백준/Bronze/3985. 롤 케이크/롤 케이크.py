import collections

l = int(input())
n = int(input())
arr =[0]* (l+1)

arr_list=[]
arr_change=[]



for i in range(1,n+1):
    start, end = map(int,input().split())
    arr_list.append(end-start)
    for k in range(start,end+1):
        if arr[k] == 0:
            arr[k] = i

for m in range(n):
    if max(arr_list) == arr_list[m]:
        print(m+1)
        break
for i in range(1,n+1):
    arr_change.append(arr.count(i))
for k in range(n):
    if max(arr_change) == arr_change[k]:
        print(k+1)
        break
