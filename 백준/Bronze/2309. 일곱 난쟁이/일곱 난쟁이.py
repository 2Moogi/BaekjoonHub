import sys
input = sys.stdin.readline

h=[]
for i in range(9):
    cm=int(input())
    h.append(cm)
h.sort()
sus=[]
arr=[]
for j in range(8):
    for k in range(j+1,9):
        if sum(h)-h[j]-h[k]==100 :
            sus.append(h[j])
            sus.append(h[k])
            break

for i in range(9):
    if sus[0] != h[i] and sus[1]!=h[i]:
        arr.append(h[i])
for i in range(7):
    print(arr[i])