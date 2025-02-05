n,k=map(int,input().split())

arr=[]

chae=[]

for i in range(2,n+1):
    arr.append(i)
while arr:
    arr.sort()
    a = arr[0]
    del arr[0]
    chae.append(a)
    for num in arr:
        if num % a == 0:
            arr.remove(num)
            chae.append(num)
print(chae[k-1])