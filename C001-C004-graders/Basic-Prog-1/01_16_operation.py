a, b, x = [int(e) for e in input().split()]

if x == 1:
    print(a + b)
elif x == 2:
    print(a - b)
elif x == 3:
    print(a * b)
else:
    print(max(a, b))