m, sort = input().split()

n=int(m)
arr=[]
for i in range(n):
    nickname = input()
    arr.append(nickname)
arr2=list(set(arr))

if sort == 'Y':
    print(len(arr2))
elif sort == 'F':
    print(len(arr2)//2)
else:
    print(len(arr2)//3)
