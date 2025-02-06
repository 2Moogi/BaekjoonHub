n = int(input())
names=[]
for _ in range(n):
    name=input().strip()
    names.append(name)

frontline=sorted(names)
revline=sorted(names,reverse=True)

if names == frontline:
    print('INCREASING')
elif names == revline:
    print('DECREASING')
else:
    print('NEITHER')