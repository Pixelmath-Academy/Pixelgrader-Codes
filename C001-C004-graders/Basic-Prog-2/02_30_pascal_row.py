n = int(input())

row = [1]
for k in range(1, n + 1):
    value = 1
    for j in range(1, k + 1):
        value = value * (n - j + 1) // j
    row.append(value)

result = " ".join(str(num) for num in row)
print(result)