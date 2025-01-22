import sys
input = sys.stdin.readline

start,end = map(int,input().split())
list=[]
cnt=0
for i in range(1,1000):
    list+=[i]*i
print(sum(list[start-1:end]))