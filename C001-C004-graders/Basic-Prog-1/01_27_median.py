data = sorted(int(e) for e in input().split())
n = len(data)
if n % 2 == 1:
    median = data[n // 2] * 1.0
else:
    median = (data[n // 2 - 1] + data[n // 2]) / 2
print(round(median,1))