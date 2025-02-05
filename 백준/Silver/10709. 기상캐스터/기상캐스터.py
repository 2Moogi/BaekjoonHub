h,w = map(int,input().split())
after=[]
for i in range(h):
    now = list(input().split())
    after += now

for i in range(h):
    cnt=0
    cloud = False
    arr=[]
    for j in range(w):
        if after[i][j] == 'c':
            cnt = 0
            cloud = True
            arr.append(cnt)
        elif after[i][j] == '.':
            if cloud == False:
                arr.append(-1)
            else:
                cnt+=1
                arr.append(cnt)
    print(' '.join(map(str, arr)))
    