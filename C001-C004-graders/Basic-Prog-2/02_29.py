results = []
n = int(input().strip())
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            results.append("(" + str(i) + "," + str(j) + "," + str(k) + ")")
print(", ".join(results))