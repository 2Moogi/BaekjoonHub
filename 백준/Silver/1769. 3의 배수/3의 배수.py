import sys
input = sys.stdin.readline

word = input().strip()

cnt = 0

while len(word) > 1:
    sum = 0
    cnt+=1
    for char in word:
        sum += int(char)
        word = str(sum)
if int(word) % 3 ==0:
    print(cnt)
    print('YES')
else:
    print(cnt)
    print('NO')
