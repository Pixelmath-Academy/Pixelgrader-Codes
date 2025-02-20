n, m = (int(e) for e in input().split())
row_sums = []
for _ in range(n):
    row = [int(e) for e in input().split()]
    row_sums.append(sum(row))
row_sums.sort()
print(row_sums)