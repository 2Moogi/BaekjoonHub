import sys
input = sys.stdin.readline

n = int(input())
classes=[]
for _ in range(n):
    mscore = list(map(int,input().split()))
    del mscore[0]
    classes.append(mscore)
k=1
for clas in classes:
    clas.sort(reverse=True)
    m_g_score = 0
    for i in range(len(clas)-1):
        m_g_score = max(clas[i] - clas[i+1],m_g_score)
    print('Class',k)
    print('Max ', max(clas),', Min ', min(clas),', Largest gap ', m_g_score,sep='')
    k+=1