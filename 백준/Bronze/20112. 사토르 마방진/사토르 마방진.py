def is_sator_square(matrix, N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != matrix[j][i]:
                return "NO"
    return "YES"

# Input
N = int(input().strip())
matrix = [input().strip() for _ in range(N)]

# Check and print result
print(is_sator_square(matrix, N))
