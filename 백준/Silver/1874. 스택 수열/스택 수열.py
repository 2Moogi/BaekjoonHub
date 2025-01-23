import sys
input = sys.stdin.readline

n=int(input())
arr=[]
arr2=[]
for _ in range(n):
    num=int(input())
    arr.append(num)

memory=arr[0]
answer=[]

for j in range(1,arr[0]+1):
    arr2.append(j)
    answer.append('+')
arr2.pop()
answer.append('-')

say='YES'
for i in range(n-1):
    if arr[i+1] > arr[i]:
        for j in range(memory+1,arr[i+1]+1):
            arr2.append(j)
            answer.append('+')
        memory=arr[i+1]
        arr2.pop()
        answer.append('-')

    elif arr[i+1] < arr[i]:
        if arr2[-1] != arr[i+1]:
            say='NO'
            break
        arr2.pop()
        answer.append('-')
if say == 'NO':
    print('NO')
else:
    for i in range(len(answer)):
        print(answer[i])