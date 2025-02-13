import sys
input = sys.stdin.readline

M = int(input())
S = set()
for i in range(M):
    cmd = input().strip()
    if cmd == 'all':
        S = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif cmd[0] == 'a' :
        a,b = cmd.split()
        S.add(b)
    elif cmd[0] == 'r':
        a,b = cmd.split()
        if b not in S:
            continue
        else:
            S.remove(b)
    elif cmd[0] == 'c':
        a,b = cmd.split()
        if b in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == 't':
        a,b = cmd.split()
        if b in S:
            S.remove(b)
        else:
            S.add(b)
    elif cmd[0] == 'e':
        S = set()
