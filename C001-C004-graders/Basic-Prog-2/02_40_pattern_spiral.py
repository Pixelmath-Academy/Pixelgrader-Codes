def spiral(n):
    grid = [['' for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            layer = min(i, j, n - 1 - i, n - 1 - j)
            grid[i][j] = "*" if layer % 2 == 0 else "-"
    
    for i in range(1, int(n / 2), 2):
        grid[i][i-1] = "-"
        grid[i+1][i] = '*'
        if n % 4 == 3 or n % 4 == 2 : grid[i+2][i+1] = "-"
    if n % 4 == 0 : grid[int(n/2)][int(n/2)-1] = "-"
    for row in grid:
        print("".join(row))

n = int(input().strip())
spiral(n)