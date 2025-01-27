n, bindo = map(int,input().split())
cnt=0
for i in range(1,n+1):
    for char in str(i):
        if char == str(bindo):
            cnt+=1
print(cnt)
