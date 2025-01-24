import sys
input = sys.stdin.readline

n,m = map(int,(input().split()))
arr = list(map(int,input().split()))
arr.sort()
all=[]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            answer = arr[i]+arr[j]+arr[k]
            if answer>m:
                break
            all.append(answer)
all.sort()
print(all[-1])