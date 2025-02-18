import sys
input = sys.stdin.readline

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input().strip()
for char in cro:
    word = word.replace(char,' ')
print(len(word))
