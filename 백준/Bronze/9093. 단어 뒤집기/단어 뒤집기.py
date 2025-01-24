TC=int(input())

for _ in range(TC):
    sen = input()
    divide=sen.split(' ')
    rev_sen=''
    for word in divide:
        for i in range(len(word)-1,-1,-1):
            rev_sen+= word[i]
        rev_sen+=' '
    print(rev_sen)
