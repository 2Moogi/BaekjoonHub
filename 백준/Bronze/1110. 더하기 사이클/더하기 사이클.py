n=input()
first_n = n
cnt=0

if len(n) == 1:
    n = str(int(n)*11)
    first_n = n
while True:
    if n == '0':
        print(1) 
        break
    elif len(str(int(n[0])+int(n[1]))) == 1:
        n = n[1] + str(int(n[0])+int(n[1]))
        cnt+=1
        if n == first_n:
            print(cnt)
            break
    else:
        n = n[1] + str(int(n[0])+int(n[1]))[1]
        cnt+=1
        if n == first_n:
            print(cnt)
            break

