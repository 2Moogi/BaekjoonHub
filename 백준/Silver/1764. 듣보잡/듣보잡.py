n,m = map(int,input().split())
dict={}
for i in range(n):
    name = input()
    dict[name] = 1
for j in range(m):
    name = input()
    if name in dict:
        dict[name] += 1
    else:
        dict[name] = 1
cnt=0
names=[]
for name in dict:
    if dict[name] == 2:
        cnt+=1
        names.append(name)
names.sort()

print(cnt)
for name in names:
    print(name)
        
    
