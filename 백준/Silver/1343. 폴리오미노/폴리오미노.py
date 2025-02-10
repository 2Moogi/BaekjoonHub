import sys
input = sys.stdin.readline

word = input().strip()
arr=[]
ans_arr=[]
answer = ''
if '.' in word:
    arr = word.split('.')
    for poli in arr:
        if len(poli) % 2 == 1:
            answer = '-1'
            break
        else:
            if len(poli) % 4 == 0:
                ans_arr.append('A' * len(poli))
            elif len(poli) > 2:
                ans_arr.append('AAAA' * (len(poli)//4) + 'B'* (len(poli) - (4*(len(poli)//4))))
            else:
                ans_arr.append('B' * len(poli))
    if answer == '-1':
        answer = '-1'
    else:
        answer = '.'.join(ans_arr)
else:
    if len(word) % 2 == 1:
        answer = '-1'
    else:
        if len(word) % 4 == 0:
            answer = 'A' * len(word)
        elif len(word) > 2:
            answer = 'AAAA' * (len(word)//4) + 'B'* (len(word) - (4*(len(word)//4)))
        else:
            answer = 'B' * len(word)
print(answer)
