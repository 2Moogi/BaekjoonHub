import sys
input = sys.stdin.readline

n = int(input())
arr =[]
for _ in range(n):
    num = input().strip()
    arr.append(num)
    
for i in range(len(arr[0])):
    nums=[]
    for ar in arr:
        nums.append(ar[-(i+1):])
    if len(nums) == len(set(nums)):
        print(i+1)
        break
            
