import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

cnt = 0
cnt_arr = []
for i in range(n-1):
    if arr[i+1] > arr[i]:
        if i == n-2:
            cnt += arr[i+1] - arr[i]
            cnt_arr.append(cnt)
            break
        else:
            cnt += arr[i+1] - arr[i]
    else:
        cnt_arr.append(cnt)
        cnt = 0
if len(cnt_arr)>1:
    print(max(cnt_arr))
else:
    print(0)
