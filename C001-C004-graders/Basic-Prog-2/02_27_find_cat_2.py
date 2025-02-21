n, m = (int(e) for e in input().split())
grid = [input().strip() for _ in range(n)]

total_count = 0

for i in range(n):
    for j in range(m):
        if j + 2 < m and grid[i][j] == 'C' and grid[i][j+1] == 'A' and grid[i][j+2] == 'T':
            total_count += 1
        if j - 2 >= 0 and grid[i][j] == 'C' and grid[i][j-1] == 'A' and grid[i][j-2] == 'T':
            total_count += 1
        if i + 2 < n and grid[i][j] == 'C' and grid[i+1][j] == 'A' and grid[i+2][j] == 'T':
            total_count += 1
        if i - 2 >= 0 and grid[i][j] == 'C' and grid[i-1][j] == 'A' and grid[i-2][j] == 'T':
            total_count += 1
        if i + 2 < n and j + 2 < m and grid[i][j] == 'C' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'T':
            total_count += 1
        if i - 2 >= 0 and j - 2 >= 0 and grid[i][j] == 'C' and grid[i-1][j-1] == 'A' and grid[i-2][j-2] == 'T':
            total_count += 1
        if i + 2 < n and j - 2 >= 0 and grid[i][j] == 'C' and grid[i+1][j-1] == 'A' and grid[i+2][j-2] == 'T':
            total_count += 1
        if i - 2 >= 0 and j + 2 < m and grid[i][j] == 'C' and grid[i-1][j+1] == 'A' and grid[i-2][j+2] == 'T':
            total_count += 1

print(total_count)