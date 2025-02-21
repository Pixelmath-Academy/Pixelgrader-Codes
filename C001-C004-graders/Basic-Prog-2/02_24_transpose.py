def transpose_matrix(n, m, matrix):
    transposed = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    return transposed

n, m = [int(e) for e in input().split()]
matrix = []
for _ in range(n):
    row = [int(e) for e in input().split()]
    matrix.append(row)

transposed_matrix = transpose_matrix(n, m, matrix)

for row in transposed_matrix:
    print(' '.join(str(e) for e in row))