x, k = input().split()
x = float(x)
k = int(k)
ans = 0.0
for i in range(1, k + 1):
    term = ((-1) ** (i + 1)) * (x ** i) / i
    ans += term
print('%.6f' % ans)