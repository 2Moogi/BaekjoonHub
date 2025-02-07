TC = int(input())

for _ in range(TC):
    gwalho = input().strip()
    num = 0
    for char in gwalho:
        if num < 0:
            answer = 'NO'
        elif char == '(':
            num +=1
        elif char == ')':
            num -=1
    if num != 0:
        answer = 'NO'
    else:
        answer = 'YES'
    print(answer)
