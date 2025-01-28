n = int(input())
m = bin(n)[2:]
rev = ''
for i in range(len(m)-1,-1,-1):
    rev += m[i]

answer = 0

for i in range(len(m)):
    answer+= int(rev[i]) * 2**(len(m)-(i+1))
print(answer)