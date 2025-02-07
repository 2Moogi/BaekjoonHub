from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
Q = deque()
for _ in range(n):
    cmd = input().strip()
    if cmd[0:6] == 'push_f':
        a,b=cmd.split()
        Q.appendleft(b)
    elif cmd[0:6] == 'push_b':
        a,b=cmd.split()
        Q.append(b)
    elif cmd[0:5] == 'pop_f':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif cmd[0:5] == 'pop_b':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.pop())
    elif cmd[0] == 's':
        print(len(Q))
    elif cmd[0] == 'e':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'f':
        if len(Q) == 0 :
            print(-1)
        else:
            print(Q[0])
    elif cmd[0] == 'b':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])
