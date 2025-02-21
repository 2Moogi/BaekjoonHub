import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = input().rstrip() # 주어지는 수
    cnt = 0

    while N != "6174":
        cnt += 1	# 단계 추가

        a = int("".join(sorted(N, reverse=True)))	# 가장 큰 수
        b = int("".join(sorted(N)))	# 가장 작은 수
        N = str(a - b)

        if len(N) < 4:	# 새로운 수의 길이가 네 자릿수가 아니라면
            for _ in range(4 - len(N)):
                N += "0"	# 0을 추가하여 네 자릿수를 맞춤

    print(cnt)
