TC = int(input())
for _ in range(TC):
    arr=input()
    count_arr=[0] * 8
    for i in range(38):
        if arr[i] == 'H':
            if arr[i+1] == 'H':
                if arr[i+2] == 'H':
                    count_arr[7] +=1
                elif arr[i+2] == 'T':
                    count_arr[6] +=1
            elif arr[i+1] == 'T':
                if arr[i+2] == 'H':
                    count_arr[5] +=1
                elif arr[i+2] == 'T':
                    count_arr[4] +=1
        elif arr[i] == 'T':
            if arr[i+1] == 'H':
                if arr[i+2] == 'H':
                    count_arr[3] +=1
                elif arr[i+2] == 'T':
                    count_arr[2] +=1
            elif arr[i+1] == 'T':
                if arr[i+2] == 'H':
                    count_arr[1] +=1
                elif arr[i+2] == 'T':
                    count_arr[0] +=1
    for i in range(8):
        if i ==7:
            print(count_arr[i])
        else:
            print(count_arr[i], end=' ')
