R, C, ZR, ZC = map(int, input().split())
for i in range(R):
    line = input().rstrip()
    enlarged_line = ""
    for ch in line:
        enlarged_line += ch * ZC
    for _ in range(ZR):
        print(enlarged_line)
