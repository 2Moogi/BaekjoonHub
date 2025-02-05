TC = int(input())
cnt=0
for _ in range(TC):
    arr=[]
    word = input()
    for i in range(len(word)):
        if word[i] in arr:
            if word[i] != word[i-1]:
                break
            elif word[i] == word[i-1] and i == len(word)-1:
                cnt+=1
        elif word[i] not in arr:
            arr.append(word[i])
            if i == len(word)-1:
                cnt+=1
        
print(cnt)
