import sys
input = sys.stdin.readline

n=int(input())
files=[]

for i in range(n):
    file = input().strip()
    files.append(file)

first_file=files[0]
answer=''

for i in range(len(files[0])):
    for j in range(len(files)):
        if files[j][i] != first_file[i]:
            answer+='?'
            break
        elif files[j][i] == first_file[i] and j==len(files)-1:
            answer+=files[j][i]
print(answer)