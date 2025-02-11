import sys

input = sys.stdin.readline

n = int(input())
scores = list(map(int,input().split()))

answer = sum(scores) / max(scores) * 100 /n
print(answer)