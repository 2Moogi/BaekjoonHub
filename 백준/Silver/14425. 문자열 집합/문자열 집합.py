n, m = map(int,input().split())

cnt = 0
A=[]
for _ in range(n):
    word= input()
    A.append(word)
A=set(A)
for _ in range(m):
    word = input()
    if word in A:
        cnt+=1
print(cnt)
