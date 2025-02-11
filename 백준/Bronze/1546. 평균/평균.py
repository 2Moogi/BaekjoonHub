import sys

input = sys.stdin.readline

n = int(input())
scores = list(map(int,input().split()))
newscores=[]
for score in scores:
    newscore = score/max(scores)*100
    newscores.append(newscore)
answer = sum(newscores)/n
print(answer)