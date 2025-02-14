import sys
input = sys.stdin.readline

hsum = 0
bsum = 0
for _ in range(20):
    a,b,c = input().split()
    if c == 'A+':
        hsum += 4.5 * float(b)
        bsum += float(b)
    elif c == 'A0':
        hsum += 4.0 * float(b)
        bsum += float(b)
    elif c == 'B+':
        hsum += 3.5 * float(b)
        bsum += float(b)
    elif c == 'B0':
        hsum += 3.0 * float(b)
        bsum += float(b)
    elif c == 'C+':
        hsum += 2.5 * float(b)
        bsum += float(b)
    elif c == 'C0':
        hsum += 2.0 * float(b)
        bsum += float(b)
    elif c == 'D+':
        hsum += 1.5 * float(b)
        bsum += float(b)
    elif c == 'D0':
        hsum += 1.0 * float(b)
        bsum += float(b)
    elif c == 'F':
        bsum += float(b)
print(hsum/bsum)