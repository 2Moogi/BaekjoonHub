import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    n = int(input())
    arr = []
    for i in range(n):
        num = int(input())
        arr.append(num)
    k = arr.index(max(arr))+1
    if arr.count(max(arr)) > 1:
        print('no winner')
    else:
        if sum(arr)/2 < max(arr):
            print('majority winner',k)
        else:
            print('minority winner',k)
