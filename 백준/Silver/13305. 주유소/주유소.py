import sys

input = sys.stdin.readline

n = int(input())
km_list = list(map(int,input().split()))
price_list = list(map(int,input().split()))
del price_list[-1]



answer = km_list[0]*price_list[0]
min_price = price_list[0]
for i in range(1,n-1):
    min_price = min(min_price,price_list[i])
    answer += km_list[i] * min_price
print(answer)