import sys
input = sys.stdin.readline

n = input().strip()

answer = (((int(n) - 10**(len(n)-1)) +1) * len(n))

for i in range(1,len(n)):
    answer += 9 * (10**(i-1)) * i
print(answer)