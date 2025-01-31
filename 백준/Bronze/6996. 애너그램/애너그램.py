TC = int(input())

for _ in range(TC):
    dict_a={}
    dict_b={}
    a,b = input().split()
    for char in a:
        if char in dict_a.keys():
            dict_a[char] += 1
        else:
            dict_a[char] = 1
    for char in b:
        if char in dict_b.keys():
            dict_b[char] += 1
        else:
            dict_b[char] = 1
    if dict_a == dict_b:
        print(a,'&',b,'are anagrams.')
    else:
        print(a,'&',b,'are NOT anagrams.')
