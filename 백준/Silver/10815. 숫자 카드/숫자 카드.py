from collections import deque
import sys
input=sys.stdin.readline

n = int(input())
arr1 = set(map(int,input().split()))

m = int(input())
arr2 = list(map(int,input().split()))

for i in arr2:
    if i in arr1:
        print(1, end=' ')
    else:
        print(0, end=' ')
