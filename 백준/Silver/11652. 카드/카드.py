import sys

input = sys.stdin.readline

n = int(input())
dict={}
for _ in range(n):
    num = int(input())
    if num in dict:
        dict[num] +=1
    else:
        dict[num] = 1
list_a=sorted(dict.items())
list_b=sorted(list_a, key=lambda x:x[1],reverse=True)
print(list_b[0][0])