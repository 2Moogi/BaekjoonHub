n,k=map(int,input().split())
coin_types=[]
for i in range(n):
    data = int(input())
    coin_types.append(data)
coin_types.reverse()
count = 0
for coin in coin_types:
        count = count + k // coin
        k = k % coin
print(count)
