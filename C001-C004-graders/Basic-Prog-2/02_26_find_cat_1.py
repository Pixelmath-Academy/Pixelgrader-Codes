n, m = (int(e) for e in input().split())
table = [input().strip() for _ in range(n)]
cat_count = 0

for i in range(n):
    for j in range(m - 2):
        if table[i][j:j+3] == "CAT":
            cat_count += 1

for j in range(m):
    for i in range(n - 2):
        if table[i][j] == 'C' and table[i+1][j] == 'A' and table[i+2][j] == 'T':
            cat_count += 1

print(cat_count)