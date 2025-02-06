TC = int(input())
arr=[]
rank=[1] * TC
for _ in range(TC):
    wei, hei = map(int,input().split())
    arr.append([wei,hei])

for i in range(TC):
    for j in range(i+1,TC):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank[i]+=1
        elif arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            rank[j]+=1
print(' '.join(map(str,rank)))