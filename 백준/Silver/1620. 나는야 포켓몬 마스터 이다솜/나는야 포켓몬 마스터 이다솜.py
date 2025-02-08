import sys

input = sys.stdin.readline
dict1={}
dict2={}
n, m = map(int,input().split())
for i in range(1,n+1):
    name = input().strip()
    dict1[name] = i
    dict2[i] = name
for i in range(m):
    name = input().strip()
    if 64< ord(name[0]) <91 or 64< ord(name[-1]) <91 :
        print(dict1[name])
    else:
        print(dict2[int(name)])