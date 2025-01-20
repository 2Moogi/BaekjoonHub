n = int(input())

dict_a = {}
cnt = 0
for i in range(n):
    num,pos = input().split()

    if num in dict_a.keys():
        if dict_a.get(num) != pos:
            cnt+=1
            dict_a[num] = pos
            
    else:
        dict_a.update({num:pos})
print(cnt)
