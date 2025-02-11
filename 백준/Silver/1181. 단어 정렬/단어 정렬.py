import sys

input = sys.stdin.readline

n = int(input())
words=[]
for _ in range(n):
    word = input().strip()
    words.append(word)
words = list(set(words))
words.sort()
words.sort(key=lambda x:len(x))
for i in words:
    print(i)