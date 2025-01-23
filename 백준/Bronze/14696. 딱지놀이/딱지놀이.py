import sys
input = sys.stdin.readline

n=int(input())

for _ in range(n):
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    del A[0]
    del B[0]

    if A.count(4)>B.count(4):
        print('A')
    elif A.count(4) < B.count(4):
        print('B')
    elif A.count(4) == B.count(4):
        if A.count(3) > B.count(3):
            print('A')
        elif A.count(3) < B.count(3):
            print('B')
        elif A.count(3) == B.count(3):
            if A.count(2) > B.count(2):
                print('A')
            elif A.count(2) < B.count(2):
                print('B')
            elif A.count(2) == B.count(2):
                if A.count(1) > B.count(1):
                    print('A')
                elif A.count(1) < B.count(1):
                    print('B')
                elif A.count(1) == B.count(1):
                    print('D')