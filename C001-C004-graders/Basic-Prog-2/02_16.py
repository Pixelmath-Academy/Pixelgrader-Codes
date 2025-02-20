n, m = [int(e) for e in input().split()]
matrix_sum = 0

for _ in range(n):
    row = [int(e) for e in input().split()]
    matrix_sum += sum(row)

print(matrix_sum)