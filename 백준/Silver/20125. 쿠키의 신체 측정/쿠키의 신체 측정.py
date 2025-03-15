n=int(input())

cookies=[]
larm,rarm,body,lleg,rleg = 0,0,0,0,0
for i in range(n):
    cookie = input()
    cookies.append(cookie)

for i in range(n):
    for j in range(n):
        if cookies[i][j] == '*':
            break
    if cookies[i][j] == '*':
        break



for k in range(j):
    if cookies[i+1][k] == '*':
        larm+=1
for k in range(j+1,n):
    if cookies[i+1][k] == '_':
        break
    else:
        rarm+=1
for k in range(i+2,n):
    if cookies[k][j] == '_':
        break
    else:
        body+=1
for m in range(k,n):
    if cookies[m][j-1] == '_':
        break
    else:
        lleg+=1
for m in range(k,n):
    if cookies[m][j+1] == '_':
        break
    else:
        rleg+=1



print(i+2,j+1)
print(larm,rarm,body,lleg,rleg)
