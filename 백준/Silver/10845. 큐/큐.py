import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
Q = deque()
for i in range(n):
    cmd = input().strip()
    if cmd[0] == 'p' and len(cmd) > 3:
        a,b=cmd.split(' ')
        Q.append(int(b))
    elif cmd[0] == 'p':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif cmd[0] == 's':
        print(len(Q))
    elif cmd[0] == 'e':
        if len(Q) == 0 :
            print(1)
        else:
            print(0)
    elif cmd[0] == 'f':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif cmd[0] == 'b':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])