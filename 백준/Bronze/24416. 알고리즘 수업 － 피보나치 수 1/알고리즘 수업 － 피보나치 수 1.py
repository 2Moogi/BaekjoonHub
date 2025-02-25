import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * (n+1)

arr[0] = 0
arr[1] = 1
cnt= 0
for i in range(2,n+1):
    cnt+=1
    arr[i] = arr[i-2]+arr[i-1]
print(arr[n], cnt-1)
