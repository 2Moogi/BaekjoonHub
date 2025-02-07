from collections import deque
n=int(input())
card=deque()
for i in range(1,n+1):
    card.append(i)
while True:
    if len(card) == 1:
        last=card.popleft()
        break
    else:
        card.popleft()
        if len(card) == 1:
            last=card.popleft()
            break
        card.append(card.popleft())
print(last)