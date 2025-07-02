n, m = map(int,input().split())
answer = 0
arr = []
for i in range(n):
    sen = input()
    arr.append(sen)

for i in range(n):
    rowcnt = 0
    for j in range(m):
        if arr[i][j] == '-':
            if j == m-1:
                answer += 1
            else:
                rowcnt += 1
        else:
            if rowcnt > 0 :
                answer += 1
                rowcnt = 0
for i in range(m):
    colcnt = 0
    for j in range(n):
        if arr[j][i] == '|':
            if j == n-1:
                answer += 1
            else:
                colcnt += 1
        else:
            if colcnt > 0 :
                answer += 1
                colcnt = 0
print(answer)