TC = int(input())

for i in range(TC):
    cnt = 0
    n,m = map(int,input().split())

    for j in range(n,m+1):
        char = str(j)

        for ch in char:
            if ch == '0':
                cnt+=1
    print(cnt)
