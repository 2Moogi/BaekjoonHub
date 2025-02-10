import sys

input = sys.stdin.readline

word = input().strip()

arr=[]

for i in range(len(word)):
    for j in range(len(word)-i):
        arr.append(word[j:j+i+1])
print(len(set(arr)))